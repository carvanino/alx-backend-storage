-- Creates a table users with unique column and an auto incremental
-- primary key and includes an ENUM constraint on a column

DROP TABLE IF EXISTS users;

CREATE TABLE IF NOT EXISTS users (
id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
email VARCHAR(255) NOT NULL UNIQUE,
name VARCHAR(255),
country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
