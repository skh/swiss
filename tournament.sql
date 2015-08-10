-- Table definitions for the tournament project.
--
-- Recreates the database from scratch. All data will be lost. 
-- To execute, call:
--  $ psql -f tournament.sql

DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;

\c tournament;

CREATE TABLE players (
    id	  serial PRIMARY KEY,
    name  varchar(40) NOT NULL
);

CREATE TABLE matches (
    winner  integer NOT NULL,
    loser  integer NOT NULL,
    PRIMARY KEY (winner, loser),
    FOREIGN KEY (winner) REFERENCES players (id),
    FOREIGN KEY (loser) REFERENCES players (id)
);

CREATE VIEW player_standings AS
    SELECT players.id, 
           players.name, 
           count(matches.winner) AS wins, 
              (SELECT count(*) 
               FROM matches 
               WHERE players.id = matches.winner
               OR players.id = matches.loser) 
           AS matches 
    FROM players 
    LEFT JOIN matches ON players.id = matches.winner 
    GROUP BY players.id;


