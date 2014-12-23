import sqlite3
import json
from flask import Flask, g, request

# Set up some application defaults
# See http://flask.pocoo.org/docs/0.10/tutorial/setup/
DATABASE = 'nbastats.db'
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


# Add methods to create a db connection when a request arrives
# and to close it afterwards.
# See http://flask.pocoo.org/docs/0.10/tutorial/dbcon
@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

# This is my custom method that will accept a `sql` parameter
# to the HTTP GET request, and executs the query
@app.route('/')
def show_entries():
    sql = request.args.get('sql', 'select * from nbastats')
    cur = g.db.execute(sql)
    entries = cur.fetchall()
    return json.dumps(entries)

# This function will run the app
if __name__ == '__main__':
    app.run()

