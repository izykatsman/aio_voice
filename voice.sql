CREATE TABLE IF NOT EXISTS `chat`(
`id` BIGINT NOT NULL unique,
`username` TEXT NULL,
PRIMARY KEY(`id`)
);

CREATE TABLE IF NOT EXISTS `user`(
`id` BIGINT NOT NULL unique,
`username` TEXT NULL,
PRIMARY KEY(`id`)
);

CREATE TABLE IF NOT EXISTS `user_in_chat`(
`chat_id` BIGINT NOT NULL,
`user_id` BIGINT NOT NULL,
FOREIGN KEY(`chat_id`) REFERENCES `chat`(`id`),
FOREIGN KEY(`user_id`) REFERENCES `user`(`id`),
PRIMARY KEY(`user_id`, `chat_id`)
);

CREATE TABLE IF NOT EXISTS `hellow`(
`id` INT NOT NULL AUTO_INCREMENT,
`text` text NULL,
image text NULL,
PRIMARY KEY(`id`)
);