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

def query_is_ok(sql):
    qok = True
    if sql[0:6] != 'select':
        qok = False
    if ';' in sql:
        qok = False
    return qok

# This is my custom method that will accept a `sql` parameter
# to the HTTP GET request, and executs the query
@app.route('/')
def show_entries():
    sql = request.args.get('sql', 'select * from nbastats')
    if query_is_ok(sql):
        cur = g.db.execute(sql)
        entries = cur.fetchall()
        return json.dumps(entries)
    else:
        return json.dumps({'error': 'you\'re query is considered to be insecure'})

# This function will run the app
if __name__ == '__main__':
    app.run()

