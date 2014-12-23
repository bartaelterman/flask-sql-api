flask-sql-api
=============

Demo on how to set up a Flask webservice that allows plain sql read access to database tables

## Goal

Create a database and an application that accepts HTTP Get calls with the `sql` parameter and returns the results of that query as json.

## Requirements

Make sure you have sqlite3, python and [Flask](http://flask.pocoo.org/docs/0.10/) installed.

## Run it yourself

### Set up the database

- `sqlite3 nbastats.db < schema.sql`: this will execute the sql statements in `schema.sql` that will create a table `nbastats`.
- `python load_data.py`: this will load the data from `data.csv` (contains some NBA sats) into the database.
- `python app.py`: runs the app. It will be accessible at [localhost:5000](http://localhost:5000/)

### Example queries

Select only players from the Indiana pacers:

```
http://localhost:5000/?sql=select name,team from nbastats where team='Ind'
```

Aggregate the points made by team:

```
http://localhost:5000/?sql=select sum(points_made),team from nbastats group by team
```

## Warning

The app currently does not stop a user from sending `drop table` or `insert` statements and is absolutely insecure. I'm looking into better ways to deal with that.
