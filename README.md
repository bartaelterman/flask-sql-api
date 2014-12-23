flask-sql-api
=============

Demo on how to set up a Flask webservice that allows plain sql read access to database tables

## Goal

Create a database and an application that accepts HTTP Get calls with the `sql` parameter and returns the results of that query as json.

## Run it yourself

### Set up the database

- `sqlite3 nbastats.db < schema.sql`: this will execute the sql statements in `schema.sql` that will create a table `nbastats`.
- `python load_data.py`: this will load the data from `data.csv` (contains some NBA sats) into the database.
