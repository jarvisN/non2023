from flask import Flask, render_template, request, session, redirect, url_for
import mariadb
from flask_dance.contrib.facebook import make_facebook_blueprint, facebook
import secrets
import hashlib

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Set up the Facebook blueprint
app.config["FACEBOOK_OAUTH_CLIENT_ID"] = "193911316826522"
app.config["FACEBOOK_OAUTH_CLIENT_SECRET"] = "67e63e4ce5e1d5d3614ec2bbe0d9ef0d"
blueprint = make_facebook_blueprint(scope="email")
app.register_blueprint(blueprint, url_prefix="/login")

# Set up the database connection details
db_host = '128.199.245.117'
db_port = 3306
db_username = 'non'
db_password = '662542'
db_database = 'login_system'

# Define the home page route


@app.route('/')
def home():
    return render_template('/html/home.html')

# Define the login route


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password = hashlib.sha256(password.encode()).hexdigest()

        # Connect to the database and retrieve the user information
        conn = mariadb.connect(
            user=db_username,
            password=db_password,
            host=db_host,
            port=db_port,
            database=db_database
        )
        cursor = conn.cursor()
        cursor.execute(
            f"SELECT username , password  FROM users WHERE username='{username}' AND password='{password}'")
        user = cursor.fetchone()

        # If the user exists, set the session user ID and redirect to the dashboard
        if user:
            session['user_id'] = user[0]
            return redirect(url_for('dashboard'))
        else:
            return render_template('html/login.html', error='Invalid username or password')
    else:
        return render_template('html/login.html')

# Define the registration route


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        password = hashlib.sha256(password.encode()).hexdigest()

        # Connect to the database and insert the new user information
        conn = mariadb.connect(
            user=db_username,
            password=db_password,
            host=db_host,
            port=db_port,
            database=db_database
        )
        cursor = conn.cursor()
        cursor.execute(
            f"INSERT INTO users (username, password, email) VALUES ('{username}', '{password}', '{email}')")
        conn.commit()

        # Redirect the user to the login page
        return redirect(url_for('login'))
    else:
        return render_template('html/register.html')

# Define the dashboard route


@app.route('/dashboard')
def dashboard():
    if not session.get('user_id'):
        return redirect(url_for('login'))
    return render_template('html/dashboard.html')

# Define the Facebook login route


@app.route('/facebook-login')
def facebook_login():
    if not facebook.authorized:
        return redirect(url_for('facebook.login'))
    resp = facebook.get('/me?fields=id,name,email')
    if not resp.ok:
        return 'Could not fetch your information from Facebook'
    user_info = resp.json()
    # Check if the user already exists in the database
    conn = mariadb.connect(
        user=db_username,
        password=db_password,
        host=db_host,
        port=db_port,
        database=db_database
    )
    cursor = conn.cursor()
    cursor.execute(
        f"SELECT username FROM users WHERE username='{user_info['email']}'")
    user = cursor.fetchone()
    # If the user exists, set the session user ID and redirect to the dashboard
    if user:
        session['user_id'] = user[0]
        return redirect(url_for('dashboard'))
    else:
        # If the user doesn't exist, create a new account and redirect to the dashboard
        cursor.execute(
            f"INSERT INTO users (username, password) VALUES ('{user_info['email']}', '')")
        conn.commit()
        session['user_id'] = user_info['email']
        return redirect(url_for('dashboard'))
