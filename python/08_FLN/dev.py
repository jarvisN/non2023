from flask import Flask, render_template, request, session, redirect
import mariadb
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Set up the database connection details
db_host = '128.199.245.117'
db_port = '3306'
db_username = 'non'
db_password = '662542'
db_database = 'login_system'

# Define the home page route
@app.route('/testNon')
def home():
    return render_template('html/home.html')

# Define the login route
@app.route('/testNon/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Connect to the database and retrieve the user information
        conn = mariadb.connect(
            user=db_username,
            password=db_password,
            host=db_host,
            port=db_port,
            database=db_database
        )
        cursor = conn.cursor()
        cursor.execute(f"SELECT username , password  FROM users WHERE username='{username}' AND password='{password}'")
        user = cursor.fetchone()

        # If the user exists, set the session user ID and redirect to the dashboard
        if user:
            session['user_id'] = user[0]
            return redirect('/dashboard')
        else:
            return render_template('html/login.html', error='Invalid username or password')
    else:
        return render_template('html/login.html')

@app.route('/testNon/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = chr(request.form['username'])
        password = chr(request.form['password'])
        email = chr(request.form['email'])
        print("\n ======================================= \n")
        print("test")
        print("\n ======================================= \n")
        print("\n ======================================= \n")
        print(type(username))
        print(type(password))
        print(type(email))
        print("\n ======================================= \n")
        
        

        # Connect to the database and insert the new user information
        conn = mariadb.connect(
            user=db_username,
            password=db_password,
            host=db_host,
            port=db_port,
            database=db_database
        )
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password, email) VALUES (%s, %s, %s)", (username, password, email))
        conn.commit()

        # Redirect the user to the login page
        return redirect('testNon/login')
    else:
        return render_template('html/register.html')

# Define the dashboard route
@app.route('/testNon/dashboard')
def dashboard():
    if 'user_id' in session:

        # Connect to the database and retrieve the user information
        conn = mariadb.connect(
            user=db_username,
            password=db_password,
            host=db_host,
            port=db_port,
            database=db_database
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id=?", (session['user_id'],))
        user = cursor.fetchone()

        # Render the dashboard template with the user information
        return render_template('html/dashboard.html', user=user)
    else:
        return redirect('/login')

if __name__ == '__main__':
    app.run()
