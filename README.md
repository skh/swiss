swiss -- the swiss tournament manager

1. Introduction

This command line tool allows you to manage a swiss-style tournament
with an arbitrary number of players and keep records of the results.

To use it, you need a running postgres database and a user who is
allowed to create databases. This README assumes that your system
behaves as described here:

  https://help.ubuntu.com/community/PostgreSQL

with a postgres user with the same name as your sysem user.

2. Setup the database

To initialize the database, run

  $ psql -f tournament.sql

If the database 'tournament' already exists, it will be dropped and
recreated.

3. Use the interactive command line tool

Run

  $ python tournament_tool.py

and follow the instructions on the screen.

4. Unit tests

To run the unit tests, run

  $ python tournament_test.py




