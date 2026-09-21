export type Word={id:number;word:string;part_of_speech:string;turkish_meaning:string;example_en:string;example_tr:string};
export type Example={en:string;tr:string};
export type Question={id:string;prompt:string;answers:string[];explanation:string};
export type Lesson={id:string;group:string;title:string;subtitle:string;intro:string;usage:string[];forms:string[];examples:Example[];tips:string[];comparison:string;questions:Question[]};
export type Verb={word:string;v2:string;v3:string;meaning:string;regular:boolean;note:string;wordId:number|null;examples:Example[]};
export type Reading={id:string;title:string;subtitle:string;lines:Example[];vocabulary:{word:string;meaning:string}[];questions:Question[]};
export type ProgressItem={item_key:string;stage:number;due:number;reviews:number;lapses:number;updated:number;last_answer:string;last_rating:string};
export type StudyState={progress:ProgressItem[];today:{words:number;lessons:number;questions:number};week:{day:string;count:number}[]};
export const normalize=(s:string)=>s.normalize("NFKC").toLowerCase().replace(/[’‘]/g,"'").replace(/\bwon't\b/g,"will not").replace(/\bcan't\b/g,"cannot").replace(/\bshan't\b/g,"shall not").replace(/\bcannot\b/g,"can not").replace(/n't\b/g," not").replace(/\bi'm\b/g,"i am").replace(/\b(you|we|they)'re\b/g,"$1 are").replace(/\b(i|you|we|they)'ve\b/g,"$1 have").replace(/\b(i|you|he|she|it|we|they)'ll\b/g,"$1 will").replace(/[.,!?;:"]/g,"").replace(/\s+/g," ").trim();
export function checkAnswer(value:string,answers:string[]){
 const variants=(s:string)=>["is","has"].flatMap(a=>["had","would"].map(b=>normalize(s).replace(/\b(he|she|it|that|there|what|who)'s\b/g,"$1 "+a).replace(/\b(i|you|he|she|it|we|they)'d\b/g,"$1 "+b)));
 const candidates=variants(value);return answers.some(a=>variants(a).some(v=>candidates.includes(v)));
}
export function chooseDeck(words:Word[],progress:ProgressItem[],now=Date.now(),limit=10){
 const map=new Map(progress.map(p=>[p.item_key,p]));
 const due=words.filter(w=>{const p=map.get("word:"+w.id);return p&&p.due<=now}).sort((a,b)=>map.get("word:"+a.id)!.due-map.get("word:"+b.id)!.due);
 const common=["ability","work","go","learn","help","take","make","time","need","find","think","know","come","see","give","want","feel","use","good","day"];
 const fresh=words.filter(w=>!map.has("word:"+w.id));
 fresh.sort((a,b)=>{const ai=common.indexOf(a.word),bi=common.indexOf(b.word);return (ai<0?999:ai)-(bi<0?999:bi)||a.id-b.id});
 return [...due,...fresh].slice(0,limit);
}
