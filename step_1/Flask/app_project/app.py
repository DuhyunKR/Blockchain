#app.py
from flask import Flask, render_template, request




#Flask 객체 인스턴스 생성
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register.html/')
def register():
    return render_template('register.html')

@app.route('/result.html', methods=['POST','GET'])
def result():
    if request.method == 'POST' :
        try :
            ID = request.form['ID']
            PW = request.form['PW']
            Name = request.form['Name']
            with sql.connect('database.db') as con:
                cur = con.cursor()

                cur.execute('INSERT INTO User (ID, PW, Name) VALUES (?,?,?)', (ID, PW, Name))
                con.commit()
                msg = '회원가입이 완료되었습니다.'
        except :
            con.rollback()
            msg = '다시 작성부탁드리겠습니다.'
        finally :
            return render_template('result.html', msg=msg)
            con.close()
    return ''
@app.route('/login.html')
def login():
    return render_template('login.html')

if __name__=='__main__':
    app.run(debug=True)