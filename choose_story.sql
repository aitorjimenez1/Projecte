
/* =========================================================
   BBDD: Choose your Story (SOLO ESTRUCTURA / SOLO TABLAS)
   - Sin INSERTS
   - Sin ENGINE=InnoDB
   ========================================================= */

DROP DATABASE IF EXISTS Choose_your_story;
CREATE DATABASE Choose_your_story
  DEFAULT CHARACTER SET utf8mb4
  DEFAULT COLLATE utf8mb4_spanish_ci;

USE Choose_your_story;

/* 1) USERS */
CREATE TABLE users (
  id_user    INT AUTO_INCREMENT PRIMARY KEY,
  username   VARCHAR(50)  NOT NULL,
  password   VARCHAR(255) NOT NULL,
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  UNIQUE (username)
);

/* 2) CHARACTERS */
CREATE TABLE characters (
  id_character INT AUTO_INCREMENT PRIMARY KEY,
  name         VARCHAR(60)  NOT NULL,
  description  VARCHAR(400) NOT NULL,
  UNIQUE (name)
);

/* 3) ADVENTURES */
CREATE TABLE adventures (
  id_adventure INT AUTO_INCREMENT PRIMARY KEY,
  title        VARCHAR(120) NOT NULL,
  description  VARCHAR(600) NOT NULL
);

/* 4) N:M ADVENTURES <-> CHARACTERS */
CREATE TABLE adventure_characters (
  id_adventure  INT NOT NULL,
  id_character  INT NOT NULL,
  PRIMARY KEY (id_adventure, id_character),
  CONSTRAINT fk_ac_adventure
    FOREIGN KEY (id_adventure) REFERENCES adventures(id_adventure)
    ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_ac_character
    FOREIGN KEY (id_character) REFERENCES characters(id_character)
    ON DELETE CASCADE ON UPDATE CASCADE
);

/* 5) STEPS */
CREATE TABLE steps (
  id_step      INT AUTO_INCREMENT PRIMARY KEY,
  id_adventure INT NOT NULL,
  step_code    VARCHAR(30)  NOT NULL,
  step_text    VARCHAR(800) NOT NULL,
  is_ending    TINYINT(1)   NOT NULL DEFAULT 0,
  ending_title VARCHAR(120) NULL,
  CONSTRAINT fk_steps_adventure
    FOREIGN KEY (id_adventure) REFERENCES adventures(id_adventure)
    ON DELETE CASCADE ON UPDATE CASCADE,
  UNIQUE (id_adventure, step_code)
);

/* 6) OPTIONS */
CREATE TABLE options (
  id_option    INT AUTO_INCREMENT PRIMARY KEY,
  id_step_from INT NOT NULL,
  option_text  VARCHAR(200) NOT NULL,
  id_step_to   INT NOT NULL,
  option_order INT NOT NULL DEFAULT 1,
  CONSTRAINT fk_options_step_from
    FOREIGN KEY (id_step_from) REFERENCES steps(id_step)
    ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_options_step_to
    FOREIGN KEY (id_step_to) REFERENCES steps(id_step)
    ON DELETE RESTRICT ON UPDATE CASCADE
);

/* 7) GAMES */
CREATE TABLE games (
  id_game      INT AUTO_INCREMENT PRIMARY KEY,
  id_user      INT NOT NULL,
  id_character INT NOT NULL,
  id_adventure INT NOT NULL,
  started_at   DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  ended_at     DATETIME NULL,
  current_step INT NOT NULL,
  CONSTRAINT fk_games_user
    FOREIGN KEY (id_user) REFERENCES users(id_user)
    ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT fk_games_character
    FOREIGN KEY (id_character) REFERENCES characters(id_character)
    ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT fk_games_adventure
    FOREIGN KEY (id_adventure) REFERENCES adventures(id_adventure)
    ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT fk_games_current_step
    FOREIGN KEY (current_step) REFERENCES steps(id_step)
    ON DELETE RESTRICT ON UPDATE CASCADE
);

/* 8) GAME_DECISIONS */
CREATE TABLE game_decisions (
  id_decision    INT AUTO_INCREMENT PRIMARY KEY,
  id_game        INT NOT NULL,
  decision_order INT NOT NULL,
  id_step        INT NOT NULL,
  id_option      INT NOT NULL,
  decided_at     DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_gd_game
    FOREIGN KEY (id_game) REFERENCES games(id_game)
    ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_gd_step
    FOREIGN KEY (id_step) REFERENCES steps(id_step)
    ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT fk_gd_option
    FOREIGN KEY (id_option) REFERENCES options(id_option)
    ON DELETE RESTRICT ON UPDATE CASCADE,
  UNIQUE (id_game, decision_order)
);
