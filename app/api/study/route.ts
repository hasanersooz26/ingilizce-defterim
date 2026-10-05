import { env } from "cloudflare:workers";
import { getChatGPTUser } from "@/app/chatgpt-auth";
import { lessons, allQuestions } from "@/content";
import { checkAnswer } from "@/lib/study";
const questions=new Map(allQuestions.map(q=>[q.id,q]));
const lessonIds=new Set(lessons.map(l=>l.id));
const reply=(data:unknown,status=200)=>Response.json(data,{status,headers:{"Cache-Control":"no-store"}});
function db(){if(!env.DB)throw Error("Storage unavailable");return env.DB}
function dayAt(ms:number){return new Intl.DateTimeFormat("en-CA",{timeZone:"Europe/Istanbul",year:"numeric",month:"2-digit",day:"2-digit"}).format(new Date(ms))}
async function snapshot(userId:string){
 const now=Date.now();
 const [p,e]=await Promise.all([db().prepare("SELECT item_key,stage,due,reviews,lapses,updated,last_answer,last_rating FROM progress WHERE user_id=?").bind(userId).all(),db().prepare("SELECT item_key,kind,at FROM events WHERE user_id=? AND at>=?").bind(userId,now-8*86400000).all()]);
 const rows=e.results as {item_key:string;kind:string;at:number}[];
 const todayRows=rows.filter(r=>dayAt(r.at)===dayAt(now));
 const count=(kind:string)=>new Set(todayRows.filter(r=>r.kind===kind).map(r=>r.item_key)).size;
 const week=Array.from({length:7},(_,i)=>{const day=dayAt(now-(6-i)*86400000);return {day,count:rows.filter(r=>dayAt(r.at)===day).length}});
 return {progress:p.results,today:{words:count("word"),lessons:count("lesson"),questions:count("question")},week};
}
export async function GET(){
 const user=await getChatGPTUser();if(!user)return reply({error:"Kaydetmek için hesabınla giriş yapmalısın."},401);
 try{return reply(await snapshot(user.userId))}catch(e){console.error("study load failed",e);return reply({error:"İlerlemen yüklenemedi. Yeniden dene."},503)}
}
export async function POST(request:Request){
 const user=await getChatGPTUser();if(!user)return reply({error:"Kaydetmek için hesabınla giriş yapmalısın."},401);
 const origin=request.headers.get("origin");
 if(origin && origin!==new URL(request.url).origin)return reply({error:"Geçersiz istek kaynağı."},403);
 let b:Record<string,unknown>;
 try{
  const parsed:unknown=await request.json();
  if(!parsed||typeof parsed!=="object"||Array.isArray(parsed))return reply({error:"Geçersiz istek."},400);
  b=parsed as Record<string,unknown>;
 }catch{return reply({error:"Geçersiz istek."},400)}
 if(!b||typeof b.requestId!=="string"||!/^[-a-zA-Z0-9]{10,80}$/.test(b.requestId))return reply({error:"Geçersiz istek kimliği."},400);
 let kind="",key="",rating="",answer="";let feedback:unknown=null;
 if(b.action==="review"&&typeof b.wordId==="number"&&Number.isInteger(b.wordId)&&b.wordId>=1&&b.wordId<=5946&&typeof b.rating==="string"&&["again","hard","good"].includes(b.rating)){
  kind="word";key="word:"+b.wordId;rating=b.rating;
 }else if(b.action==="completeLesson"&&typeof b.lessonId==="string"&&lessonIds.has(b.lessonId)){
  kind="lesson";key="lesson:"+b.lessonId;rating="good";
 }else if(b.action==="answer"&&questions.has(b.questionId)&&typeof b.answer==="string"&&b.answer.trim().length>0&&b.answer.length<=600){
  const q=questions.get(b.questionId)!;const correct=b.selfCorrect===true||checkAnswer(b.answer,q.answers);
  kind="question";key="question:"+q.id;rating=correct?"good":"again";answer=b.answer;
  feedback={correct,answers:q.answers,explanation:q.explanation};
 }else return reply({error:"Geçersiz çalışma kaydı."},400);
 const now=Date.now();
 // The conditional upsert precedes the event in an atomic D1 batch: retries cannot advance a card twice.
 const nextStage=rating==="again"?"0":rating==="hard"?"progress.stage":"MIN(6,progress.stage+1)";
 const nextDelay=rating==="again"?"600000":rating==="hard"?"86400000":"CASE progress.stage WHEN 0 THEN 86400000 WHEN 1 THEN 259200000 WHEN 2 THEN 604800000 WHEN 3 THEN 1209600000 WHEN 4 THEN 2592000000 ELSE 5184000000 END";
 const initialStage=rating==="good"?1:0, initialDelay=rating==="again"?600000:86400000;
 try{
 await db().batch([
 db().prepare(`INSERT INTO progress(user_id,item_key,stage,due,reviews,lapses,updated,last_answer,last_rating)
 SELECT ?,?,?,?,1,?,?,?,? WHERE NOT EXISTS(SELECT 1 FROM events WHERE user_id=? AND id=?)
 ON CONFLICT(user_id,item_key) DO UPDATE SET stage=${nextStage},due=?+${nextDelay},reviews=progress.reviews+1,lapses=progress.lapses+?,updated=?,last_answer=?,last_rating=?`).bind(user.userId,key,initialStage,now+initialDelay,rating==="again"?1:0,now,answer,rating,user.userId,b.requestId,now,rating==="again"?1:0,now,answer,rating),
 db().prepare("INSERT OR IGNORE INTO events(id,user_id,item_key,kind,rating,at) VALUES(?,?,?,?,?,?)").bind(b.requestId,user.userId,key,kind,rating,now)
 ]);
 return reply({state:await snapshot(user.userId),feedback});
 }catch(e){console.error("study save failed",e);return reply({error:"Cevabın kaydedilemedi. Sayfayı kapatmadan yeniden dene."},503)}
}
