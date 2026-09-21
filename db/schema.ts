import { sqliteTable, text, integer, primaryKey, index } from "drizzle-orm/sqlite-core";
export const progress = sqliteTable("progress", {
 userId:text("user_id").notNull(), itemKey:text("item_key").notNull(),
 stage:integer("stage").notNull().default(0), due:integer("due").notNull().default(0),
 reviews:integer("reviews").notNull().default(0), lapses:integer("lapses").notNull().default(0),
 updated:integer("updated").notNull().default(0), lastAnswer:text("last_answer").notNull().default(""),
 lastRating:text("last_rating").notNull().default("")
},t=>[primaryKey({columns:[t.userId,t.itemKey]})]);
export const events = sqliteTable("events", {
 id:text("id").notNull(),userId:text("user_id").notNull(),itemKey:text("item_key").notNull(),
 kind:text("kind").notNull(),rating:text("rating").notNull(),at:integer("at").notNull()
},t=>[primaryKey({columns:[t.userId,t.id]}),index("events_user_at").on(t.userId,t.at)]);
