import sqlite3
import csv

datafile = 'data.csv'
database = 'nbastats.db'

db = sqlite3.connect(database)
cur = db.cursor()
reader = csv.reader(open(datafile), delimiter=',')
header = reader.next()
for row in reader:
    cur.execute('insert into nbastats (date, name, team, opposite_team, points_made) values (?, ?, ?, ?, ?)', row)
db.commit()
db.close()
