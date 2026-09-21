import test from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import { checkAnswer, chooseDeck } from "../lib/study.ts";
const read=p=>JSON.parse(fs.readFileSync(new URL("../"+p,import.meta.url),"utf8"));
const words=read("public/words.json"),lessons=read("content/lessons.json"),verbs=read("content/verbs.json"),readings=read("content/readings.json");
test("content has the promised coverage and valid dictionary links",()=>{
 assert.equal(words.length,5946);assert.equal(lessons.filter(l=>l.group==="tenses").length,12);assert.equal(verbs.length,60);
 const ids=new Set();for(const l of lessons){assert.ok(!ids.has(l.id));ids.add(l.id);for(const field of ["title","subtitle","intro","comparison"])assert.ok(l[field].trim());for(const field of ["usage","forms","tips","questions"])assert.ok(l[field].length);assert.ok(l.examples.length>0);if(l.group==="tenses")assert.ok(l.examples.length>=15);}
 for(const v of verbs){const linked=words.find(w=>w.id===v.wordId);assert.equal(linked?.word,v.word);assert.ok(linked.part_of_speech.includes("verb"));assert.equal(v.examples.length,3);}
 const examples=[...lessons.flatMap(l=>l.examples),...verbs.flatMap(v=>v.examples),...readings.flatMap(r=>r.lines)];
 for(const ex of examples){assert.ok(ex.en.trim());assert.ok(ex.tr.trim());assert.notEqual(ex.en,ex.tr);assert.ok(!/[�\u0000-\u0008]/.test(ex.en+ex.tr));}
 const qs=[...lessons.flatMap(l=>l.questions),...readings.flatMap(r=>r.questions),...read("content/exercises.json")];assert.equal(new Set(qs.map(q=>q.id)).size,qs.length);
 for(const q of qs){assert.ok(q.prompt&&q.explanation&&q.answers.length);for(const a of q.answers)assert.equal(checkAnswer(a,q.answers),true);}
});
test("fair answer checks allow case, punctuation, contractions and alternatives",()=>{
 for(const [value,answers] of [["  I WON’T go. ",["I will not go"]],["She's finished.",["She has finished."]],["She's tired",["She is tired."]],["I'd help.",["I would help"]],["I didn’t go.",["I did not go."]],["He works every day.",["She works every day.","He works every day."]]])assert.equal(checkAnswer(value,answers),true,value);
 assert.equal(checkAnswer("She go",["She goes"]),false);
 assert.equal(checkAnswer("I will go",["I will not go"]),false);
 assert.equal(checkAnswer("",["went"]),false);
});
test("daily deck prioritises due items, excludes future reviews and uses distinct records",()=>{
 const small=words.slice(0,25),now=1000000;
 const mk=(id,due)=>({item_key:"word:"+id,due,stage:1,reviews:1,lapses:0,updated:0,last_answer:"",last_rating:"good"});
 const p=[mk(small[0].id,now+100),mk(small[1].id,now-10),mk(small[2].id,now-100)];
 const d=chooseDeck(small,p,now,10);
 assert.equal(d.length,10);assert.equal(d[0].id,small[2].id);assert.equal(d[1].id,small[1].id);assert.ok(!d.some(w=>w.id===small[0].id));assert.equal(new Set(d.map(w=>w.id)).size,10);
 assert.deepEqual(chooseDeck(small,small.map(w=>mk(w.id,now+100)),now),[]);
});
