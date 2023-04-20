from flask import Flask, render_template, request, session, redirect
import mariadb
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = mariadb.connect(
            user='your_db_username',
            password='your_db_password',
            host='your_db_host',
            port='your_db_port',
            database='login_system'
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()
        if user:
            session['user_id'] = user[0]
            return redirect('/dashboard')
        else:
            return render_template('login.html', error='Invalid username or password')
    else:
        return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = mariadb.connect(
            user='your_db_username',
            password='your_db_password',
            host='your_db_host',
            port='your_db_port',
            database='login_system'
        )
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        return redirect('/login')
    else:
        return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        conn = mariadb.connect(
            user='your_db_username',
            password='your_db_password',
            host='your_db_host',
            port='your_db_port',
            database='login_system'
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id=?", (session['user_id'],))
        user = cursor.fetchone()
        return render_template('dashboard.html', user=user)
    else:
        return redirect('/login')

if __name__ == '__main__':
    app.run()
