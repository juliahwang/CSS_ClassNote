from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index(name=None):
    return render_template("index.html")

@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route('/postuser', methods = ['POST', 'GET'])
def postuser():
    if request.method == 'POST':
        try:
            name = request.form['name']
            # 지역변수      플라스크 메소드 내에서 쓸 수 있는 문법
            age = request.form['age']
            email = request.form['email']
            
            with lite.connect("users.db") as conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO user (name, age, email) VALUES(?, ?, ?)", (name, age, email))
                #어트리뷰트 설정
                conn.commit()
                msg = "Signup complete"
        
        except:
            conn.rollback()
            msg = "Signup Failed"
            
        finally:
            return render_template("signup.html", msg=msg)
            
    
# 데이터 테이블 보여주기
@app.route('/users')   
def users():          # 개인정보를 처리할 때는 url이 user_~로 바뀌도록할 것이므로 s를 붙임
    conn = list.connect("users.db")
    conn.row_factory = lite.Row
    # flask의 row와 sqlite3의 row와 등치시킨다.
    
    cur = conn.cursor()
    cur.execute("SELECT * from user")
    
    rows = cur.fetchall()
    return render_template("users.html", rows = rows)


    return render_template("users.html")


if __name__ == '__main__':
    app.run(host = '0.0.0.0')