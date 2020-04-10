#!C:\Users\Pars\AppData\Local\Programs\Python\Python38-32\python.exe
from flask import Flask

app = Flask(__name__)

@app.route('/')
def show_entries():
    db = get_db()
    cursor = db.execute('SELECT * FROM entries ORDER BY i1 ASC')
   
    for row in cursor:
        #print(row)
        #print(dict(row))
        #print(row['t1'])
        #print(row['i1'])
        print(row['t1'], row['i1'], row['title'])
    return render_template('home.html', entries=entries)