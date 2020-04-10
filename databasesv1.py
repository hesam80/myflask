#!C:\Users\Pars\AppData\Local\Programs\Python\Python38-32\python.exe

import sqlite3


db = sqlite3.connect('title.db')
db.row_factory = sqlite3.Row
db.execute('DROP TABLE IF EXISTS entries')
db.execute('CREATE TABLE entries(t1 text, i1 int, title text)')

db.execute('INSERT INTO entries (t1, i1 , title) VALUES (?, ?, ?)', ('one', 1, 'hello'))
db.execute('INSERT INTO entries (t1, i1, title) VALUES (?, ?, ?)', ('two', 2, 'yes'))
db.execute('INSERT INTO entries (t1, i1, title) VALUES (?, ?, ?)', ('three', 3, 'hesam'))
db.execute('INSERT INTO entries (t1, i1, title) VALUES (?, ?, ?)', ('four', 4, 'is'))
db.execute('INSERT INTO entries (t1, i1, title) VALUES (?, ?, ?)', ('five', 5, 'best'))

db.commit()

cursor = db.execute('SELECT * FROM entries ORDER BY i1 ASC')
   
for row in cursor:
    #print(row)
    #print(dict(row))
    #print(row['t1'])
    #print(row['i1'])
    print(row['t1'], row['i1'], row['title'])
    #print(list(row))
    #print(tuple(row))


