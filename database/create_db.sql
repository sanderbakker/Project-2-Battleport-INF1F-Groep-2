CREATE DATABASE battleport;
USE battleport;

CREATE TABLE players (
  player_id int NOT NULL AUTO_INCREMENT,
  player_name varchar(30),
  password varchar(64),
  score int,
  PRIMARY KEY (player_id)
);


CREATE TABLE saves (
  save_id int NOT NULL AUTO_INCREMENT,
  save_name varchar(255),
  PRIMARY KEY (save_id)
);

CREATE TABLE saved_players (
  saved_player_id int NOT NULL AUTO_INCREMENT,
  save_id int,
  player_id int NOT NULL,
  FOREIGN KEY (player_id) REFERENCES player(player_id),
  FOREIGN KEY (save_id) REFERENCES saves(save_id),
  PRIMARY KEY (saved_player_id)
);

CREATE TABLE saved_cards (
  saved_card_id int NOT NULL AUTO_INCREMENT, 
  save_id int,
  saved_player_id int,  
  saved_card_name varchar(32),
  FOREIGN KEY (save_id) REFERENCES saves(save_id),
  FOREIGN KEY (saved_player_id) REFERENCES saved_players(saved_player_id),  
  PRIMARY KEY (saved_card_id)
); 

CREATE TABLE saved_score (
  saved_score_id int NOT NULL,
  save_id int,
  saved_player_id int,
  score int,
  FOREIGN KEY (save_id) REFERENCES saves(save_id),
  FOREIGN KEY (saved_player_id) REFERENCES saved_players(saved_player_id),
  PRIMARY KEY (saved_score_id)
); 

CREATE TABLE saved_ships (
  saved_ship_id int NOT NULL AUTO_INCREMENT,
  save_id int,
  saved_player_id int,  
  ship_name varchar(32),
  x int,
  y int,
  card_id int,
  FOREIGN KEY (save_id) REFERENCES saves(save_id),
  FOREIGN KEY (saved_player_id) REFERENCES saved_players(saved_player_id),  
  PRIMARY KEY (saved_ship_id)
); 