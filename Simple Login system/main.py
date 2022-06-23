from flask import Flask, redirect, url_for, request, render_template
import sqlite3

# my_conn = sqlite3.connect('users.db')
# my_cur = my_conn.cursor()
# query1 = 'CREATE TABLE Users(FIRST_NAME TEXT NOT NULL, LAST_NAME TEXT NOT NULL, ' \
#          'CONTACT INT NOT NULL, AGE INT, PASSWORD TEXT NOT NULL) '
# my_cur.execute(query1)
# print('Successful')
# my_conn.close()
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/register')
def register():
    return render_template('Form1.html')


@app.route('/success', methods=['POST', 'GET'])
def Success_Reg():
    if request.method == 'POST':
        try:
            first_name = request.form['fn']
            last_name = request.form['ln']
            ph_no = request.form['4n']
            age = request.form['age']
            password = request.form['pw']
            with sqlite3.connect('users.db') as my_conn:
                cur = my_conn.cursor()
                cur.execute('INSERT INTO Users(FIRST_NAME, LAST_NAME, CONTACT, AGE, PASSWORD) VALUES (?,?,?,?,?)',
                            (first_name, last_name, ph_no, age, password))
                my_conn.commit()
                status = 'RECORD SUCCESSFULLY ADDED'
        except:
            my_conn.rollback()
            status = "ERROR IN INSERT OPERATION"
        finally:
            my_conn.close()
            return render_template('result.html', msg=status)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/login_check', methods=['POST', 'GET'])
def user_check():
    if request.method == 'POST':
        u_name = request.form['un']
        u_passw = request.form['pw']
        data = (u_name, u_passw)
        with sqlite3.connect('users.db') as my_conn:
            cur = my_conn.cursor()
            cur.execute('SELECT FIRST_NAME , PASSWORD FROM Users WHERE FIRST_NAME = ? AND PASSWORD = ? ', data)
            result = cur.fetchall()
            if len(result) == 0:
                return render_template('invalid_user.html')
            else:
                return redirect(url_for('welcome', name=u_name))


@app.route('/User/<name>')
def welcome(name):
    return 'You are logged in as %s' % name


@app.route('/user_data')
def User_Info():
    with sqlite3.connect('users.db') as my_conn:
        my_conn.row_factory = sqlite3.Row
        cur = my_conn.cursor()
        query1 = 'SELECT * FROM Users'
        cur.execute(query1)
        rows = cur.fetchall()
    return render_template('userdata.html', rows=rows)


@app.route('/admin')
def Valid_admin():
    return render_template('admin.html')


@app.route('/validate_admin', methods=['POST', 'GET'])
def real_admin():
    if request.method == 'POST':
        user = request.form['admin']
        if user == 'admin':
            return redirect(url_for('User_Info'))
        else:
            return render_template('not_admin.html')


if __name__ == '__main__':
    app.run(debug=True)
