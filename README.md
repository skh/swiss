To initialize the database, have a postgresql instance running and
run

  $ psql -f tournament.sql

If the database 'tournament' already exists, it will be dropped and
recreated.

To run the unit tests, run

  $ python tournament_test.py

To run the interactive command line tool, run

  $ python tournament_tool.py


