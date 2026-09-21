"use client";
import { useEffect } from "react";
import { lessons } from "@/content";
import type { Word } from "@/lib/study";
export function useStudyTools(words:Word[],go:(view:string)=>void){
 useEffect(()=>{
  const context=(document as Document & {modelContext?:{registerTool:(tool:unknown,options:{signal:AbortSignal})=>unknown}}).modelContext;
  if(!context?.registerTool||!words.length)return;
  const life=new AbortController();
  const register=(tool:unknown)=>{try{void Promise.resolve(context.registerTool(tool,{signal:life.signal})).catch(()=>{})}catch{}};
  register({name:"search_dictionary",title:"Kelime defterinde ara",description:"Search the English-Turkish dictionary. Returns at most twenty word records; does not change study progress.",inputSchema:{type:"object",properties:{query:{type:"string",minLength:1,maxLength:100}},required:["query"],additionalProperties:false},annotations:{readOnlyHint:true,untrustedContentHint:true},execute:async(input:unknown)=>{
   const q=(input as {query?:unknown})?.query;if(typeof q!=="string"||!q.trim()||q.length>100)throw Error("1–100 karakter arasında bir arama yaz.");
   const query=q.toLocaleLowerCase("tr").replace(/ı/g,"i").trim();
   return words.filter(w=>(w.word+" "+w.turkish_meaning).toLocaleLowerCase("tr").replace(/ı/g,"i").includes(query)).slice(0,20);
  }});
  register({name:"open_lesson",title:"Bir ders aç",description:"Open a lesson in the visible app. Does not complete the lesson or change learning progress.",inputSchema:{type:"object",properties:{lessonId:{type:"string",enum:lessons.map(l=>l.id)}},required:["lessonId"],additionalProperties:false},annotations:{readOnlyHint:false,untrustedContentHint:false},execute:async(input:unknown)=>{
   const id=(input as {lessonId?:unknown})?.lessonId;if(typeof id!=="string"||!lessons.some(l=>l.id===id))throw Error("Geçerli bir ders seç.");
   go("lesson/"+id);await new Promise<void>(resolve=>requestAnimationFrame(()=>requestAnimationFrame(()=>resolve())));
   return {openedLessonId:id,title:lessons.find(l=>l.id===id)!.title};
  }});
  return ()=>life.abort();
 },[words,go]);
}
