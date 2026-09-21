CREATE TABLE `events` (
	`id` text NOT NULL,
	`user_id` text NOT NULL,
	`item_key` text NOT NULL,
	`kind` text NOT NULL,
	`rating` text NOT NULL,
	`at` integer NOT NULL,
	PRIMARY KEY(`user_id`, `id`)
);
--> statement-breakpoint
CREATE INDEX `events_user_at` ON `events` (`user_id`,`at`);--> statement-breakpoint
CREATE TABLE `progress` (
	`user_id` text NOT NULL,
	`item_key` text NOT NULL,
	`stage` integer DEFAULT 0 NOT NULL,
	`due` integer DEFAULT 0 NOT NULL,
	`reviews` integer DEFAULT 0 NOT NULL,
	`lapses` integer DEFAULT 0 NOT NULL,
	`updated` integer DEFAULT 0 NOT NULL,
	`last_answer` text DEFAULT '' NOT NULL,
	`last_rating` text DEFAULT '' NOT NULL,
	PRIMARY KEY(`user_id`, `item_key`)
);
