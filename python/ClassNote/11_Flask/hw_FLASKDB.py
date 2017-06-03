import sqlite3 as lite
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def bring_db(name=None):
    conn = lite.connect('dongari.db')
    cur = conn.cursor()
    cur.execute("SELECT * from members")
    rows = cur.fetchall()
    
    for row in rows:
        print(row)
    conn.close()

def render(name=None):
    return render_template("dongari_index.html", name = name)


if __name__ == '__main__':
    app.run(host = '0.0.0.0')