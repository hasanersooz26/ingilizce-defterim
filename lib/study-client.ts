import { Capacitor } from "@capacitor/core";
import { allQuestions, lessons } from "@/content";
import { checkAnswer, type StudyState } from "@/lib/study";

type MobileStore = {
  progress: StudyState["progress"];
  events: { id: string; item_key: string; kind: string; at: number }[];
  requests: string[];
};

const STORE_KEY = "english-study-mobile-v1";
const blankStore = (): MobileStore => ({ progress: [], events: [], requests: [] });

function readStore(): MobileStore {
  try {
    const saved = localStorage.getItem(STORE_KEY);
    if (!saved) return blankStore();
    const value = JSON.parse(saved) as Partial<MobileStore>;
    return {
      progress: Array.isArray(value.progress) ? value.progress : [],
      events: Array.isArray(value.events) ? value.events : [],
      requests: Array.isArray(value.requests) ? value.requests : [],
    };
  } catch {
    return blankStore();
  }
}

function writeStore(store: MobileStore) {
  localStorage.setItem(STORE_KEY, JSON.stringify(store));
}

function dayAt(ms: number) {
  return new Intl.DateTimeFormat("en-CA", {
    timeZone: "Europe/Istanbul", year: "numeric", month: "2-digit", day: "2-digit",
  }).format(new Date(ms));
}

function snapshot(store: MobileStore): StudyState {
  const now = Date.now();
  const events = store.events.filter((event) => event.at >= now - 8 * 86400000);
  const todayEvents = events.filter((event) => dayAt(event.at) === dayAt(now));
  const count = (kind: string) => new Set(todayEvents.filter((event) => event.kind === kind).map((event) => event.item_key)).size;
  return {
    progress: store.progress,
    today: { words: count("word"), lessons: count("lesson"), questions: count("question") },
    week: Array.from({ length: 7 }, (_, index) => {
      const day = dayAt(now - (6 - index) * 86400000);
      return { day, count: events.filter((event) => dayAt(event.at) === day).length };
    }),
  };
}

function response(data: unknown, status = 200) {
  return new Response(JSON.stringify(data), { status, headers: { "Content-Type": "application/json" } });
}

async function mobileStudyFetch(input: RequestInfo | URL, init?: RequestInit): Promise<Response> {
  if (!Capacitor.isNativePlatform() || String(input) !== "/api/study") return fetch(input, init);
  let store = readStore();
  if (!init?.method || init.method === "GET") return response(snapshot(store));

  let body: Record<string, unknown>;
  try { body = JSON.parse(String(init.body ?? "{}")) as Record<string, unknown>; }
  catch { return response({ error: "Geçersiz istek." }, 400); }
  const requestId = typeof body.requestId === "string" ? body.requestId : "";
  if (!/^[a-zA-Z0-9-]{10,80}$/.test(requestId)) return response({ error: "Geçersiz istek kimliği." }, 400);
  if (store.requests.includes(requestId)) return response({ state: snapshot(store), feedback: null });

  let kind = "", key = "", rating = "", answer = "", feedback: unknown = null;
  if (body.action === "review" && Number.isInteger(body.wordId) && Number(body.wordId) >= 1 && Number(body.wordId) <= 5946 && ["again", "hard", "good"].includes(String(body.rating))) {
    kind = "word"; key = `word:${body.wordId}`; rating = String(body.rating);
  } else if (body.action === "completeLesson" && lessons.some((lesson) => lesson.id === body.lessonId)) {
    kind = "lesson"; key = `lesson:${body.lessonId}`; rating = "good";
  } else if (body.action === "answer" && typeof body.questionId === "string" && typeof body.answer === "string" && body.answer.trim().length > 0 && body.answer.length <= 600) {
    const question = allQuestions.find((item) => item.id === body.questionId);
    if (!question) return response({ error: "Geçersiz çalışma kaydı." }, 400);
    kind = "question"; key = `question:${question.id}`; answer = body.answer;
    const correct = body.selfCorrect === true || checkAnswer(answer, question.answers);
    rating = correct ? "good" : "again";
    feedback = { correct, answers: question.answers, explanation: question.explanation };
  } else return response({ error: "Geçersiz çalışma kaydı." }, 400);

  const now = Date.now();
  const existing = store.progress.find((item) => item.item_key === key);
  const oldStage = existing?.stage ?? 0;
  const stage = rating === "again" ? 0 : rating === "hard" ? oldStage : existing ? Math.min(6, oldStage + 1) : 1;
  const delay = rating === "again" ? 600000 : rating === "hard" ? 86400000 : [86400000, 259200000, 604800000, 1209600000, 2592000000, 5184000000][Math.min(oldStage, 5)];
  const progress = {
    item_key: key, stage, due: now + delay, reviews: (existing?.reviews ?? 0) + 1,
    lapses: (existing?.lapses ?? 0) + (rating === "again" ? 1 : 0), updated: now,
    last_answer: answer, last_rating: rating,
  };
  store.progress = existing ? store.progress.map((item) => item.item_key === key ? progress : item) : [...store.progress, progress];
  store.events = [...store.events, { id: requestId, item_key: key, kind, at: now }].filter((event) => event.at >= now - 8 * 86400000);
  store.requests = [...store.requests.slice(-499), requestId];
  writeStore(store);
  return response({ state: snapshot(store), feedback });
}

export const studyFetch = mobileStudyFetch;
