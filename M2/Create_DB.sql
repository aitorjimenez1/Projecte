DROP SCHEMA IF EXISTS choose_your_story;
CREATE SCHEMA choose_your_story COLLATE = utf8_general_ci;
USE choose_your_story;

CREATE TABLE users (
    id_user INT,
    username VARCHAR(10),
    password VARCHAR(12),
    creado DATETIME,
    creador VARCHAR(40),
    modificado DATETIME,
    modificador VARCHAR(40)
);

CREATE TABLE characters (
    id_character INT,
    name VARCHAR(20),
    creado DATETIME,
    creador VARCHAR(40),
    modificado DATETIME,
    modificador VARCHAR(40)
);

CREATE TABLE adventure (
    id_adventure INT,
    name VARCHAR(40),
    description VARCHAR(2000),
    creado DATETIME,
    creador VARCHAR(40),
    modificado DATETIME,
    modificador VARCHAR(40)
);

CREATE TABLE adventure_character (
    id_character INT,
    id_adventure INT,
    creado DATETIME,
    creador VARCHAR(40),
    modificado DATETIME,
    modificador VARCHAR(40)
);

CREATE TABLE bystep_adventure (
    id_bystep_adventure INT,
    id_adventure INT,
    description VARCHAR(4000),
    answers_in_step INT,
    final_step TINYINT,
    creado DATETIME,
    creador VARCHAR(40),
    modificado DATETIME,
    modificador VARCHAR(40)
);

CREATE TABLE answers_bystep_adventure (
    id_answers_bystep_adventure INT,
    id_bystep_adventure INT,
    description VARCHAR(2000),
    resolution_answer VARCHAR(200),
    nextstep_adventure INT,
    creado DATETIME,
    creador VARCHAR(40),
    modificado DATETIME,
    modificador VARCHAR(40)
);

CREATE TABLE game (
    id_game INT,
    id_user INT,
    id_character INT,
    id_adventure INT,
    date_game DATETIME
    creado DATETIME,
    creador VARCHAR(40),
    modificado DATETIME,
    modificador VARCHAR(40)
);

CREATE TABLE choices (
    id_choice INT,
    id_game INT,
    id_bystep_adventure INT,
    id_answers_bystep_adventure INT
    creado DATETIME,
    creador VARCHAR(40),
    modificado DATETIME,
    modificador VARCHAR(40)
);