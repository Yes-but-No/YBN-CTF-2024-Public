from flask import Flask, request, jsonify, render_template,g, session,redirect,url_for
import sqlite3
import uuid 
from encrypt import encrypt,decrypt
import os 
import re 
import secrets
import string

def generate_password(length=16):
    # Define the character set
    characters = string.ascii_letters + string.digits
    # Generate a random password
    return ''.join(secrets.choice(characters) for _ in range(length))

with open("session.sql") as f:
    script = f.read()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'dev_key')
FLAG1 = os.getenv('FLAG1', 'FIRSTFLAG{this_is_a_fake_flag}')
FLAG2 = os.getenv('FLAG2', 'SECONDFLAG{this_is_a_fake_flag}')

import re

def detect_sqli(sql):
    # List of common SQL keywords and characters often used in SQL injection
    disallowed_patterns = [
        r"SELECT", r"UNION", r"JOIN", r"FROM", r"WHERE", r"ON",
        r"OR", r"AND", r"NOT", r"IN", r"LIKE", r"DROP", r"INSERT",
        r"DELETE", r"UPDATE", r"EXEC", r"EXECUTE", r"CREATE", r"ALTER",
        "--", "#", ";", "/*", "*/", "@@", "0x", "'", "\"", "`", "-", "/", "*"
    ]

    # Escape special characters and combine patterns into a single regex
    escaped_patterns = [re.escape(pattern) if not pattern.isalnum() else pattern for pattern in disallowed_patterns]
    combined_pattern = re.compile("|".join(escaped_patterns), re.IGNORECASE)

    # Check if any disallowed pattern is found in the SQL query
    if combined_pattern.search(sql):
        return True

    return False


def connect(uuid):
    conn = sqlite3.connect('databases/' + uuid + '.db')
    return conn    

def connect_users():
    conn = sqlite3.connect('users.db')
    return conn

def validate_user(conn,username,password):
    KEY,SALT,IV = get_crypto(g.uuid)
    cursor = conn.execute("SELECT userId,password,admin from users WHERE username = ?",(username,))
    user = cursor.fetchone()
    if user:
        pw = decrypt(KEY,IV,user[1])
        if 'error' in pw:
            return {"user":None,"admin":0}
        if pw['plaintext'] == password+SALT:
            return {"user":user[0],"admin":user[2]}
    return {"user":None,"admin":0}

def insert_user(conn,username,password,admin=0):
    KEY,SALT,IV = get_crypto(g.uuid)
    cursor = conn.execute("SELECT 1 from users WHERE username = ?",(username,))
    if cursor.fetchone():
        return False 
    enc_pw = encrypt(KEY,SALT,IV,password)
    if 'error' in enc_pw:
        return False
    enc_pw = enc_pw['ciphertext']
    cursor = conn.execute("INSERT INTO users(username,password,admin) VALUES (?,?,?)",(username,enc_pw,admin))
    userId = cursor.lastrowid
    conn.commit()
    return userId
    
def hire_request(uuid,userid, hitwoman, target, reason, date_of_disposal):
    with connect(uuid) as conn:
        cursor = conn.execute("INSERT INTO hire_request(userId, hitWoman,dateOfDisposal,targetName,reason) VALUES (?,?,?,?,?)",(userid,hitwoman,date_of_disposal,target,reason))
        conn.commit()
        return cursor.lastrowid

def generate_new_uuid():
    new_uuid = str(uuid.uuid4())
    with connect_users() as conn:
        cursor = conn.execute("SELECT 1 from users WHERE uuid = ?",(new_uuid,))
        if cursor.fetchone():
            return generate_new_uuid()
        
    conn = sqlite3.connect('databases/' + new_uuid + '.db')     
    conn.executescript(script)
    conn.commit()
    return new_uuid
    
def get_crypto(uuid):
    with connect_users() as conn:
        cursor = conn.execute("SELECT key,salt,iv from users WHERE uuid = ?",(uuid,))
        return cursor.fetchone()

def check_valid_uuid(uuid):
    with connect_users() as conn:
        cursor = conn.execute("SELECT 1 from users WHERE uuid = ?",(uuid,))
        return cursor.fetchone()
    
def create_new_instance():
    new_uuid = generate_new_uuid()
    g.uuid = new_uuid
    SALT = generate_password(16)
    KEY = secrets.token_bytes(32)
    IV = secrets.token_bytes(16)
    with connect_users() as conn:
        conn.execute("INSERT INTO users(uuid,key,salt,iv) VALUES (?,?,?,?)",(new_uuid,KEY,SALT,IV))
        conn.commit()
    with connect(new_uuid) as conn:
        insert_user(conn,"admin",SALT,1)
        insert_user(conn,FLAG1,SALT,0)
    return new_uuid


@app.before_request
def before_request():
    if 'uuid' not in request.cookies:
        create_new_instance()
    else:
        if not check_valid_uuid(request.cookies['uuid']):
            print("Invalid UUID",request.cookies['uuid'])
            create_new_instance()
        else:
            g.uuid = request.cookies['uuid']

@app.after_request
def after_request(response):
    if hasattr(g, 'uuid'):
        response.set_cookie('uuid', g.uuid)
    return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=["POST","GET"])
def signup():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        with connect(g.uuid) as conn:
            user_id = insert_user(conn,username,password,0)
            if user_id:
                session['is_logged_in'] = True
                session['user_id'] = user_id


        return render_template('signup.html',success=user_id, display = True)
    return render_template('signup.html')

@app.route('/login', methods = ["POST","GET"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        with connect(g.uuid) as conn:
            user = validate_user(conn,username,password)
            if user['user']:
                session['is_logged_in'] = True
                session['user_id'] = user['user']
                session['admin'] = user['admin']
        return render_template('login.html',success=user['user'], display = True)
    return render_template('login.html')


@app.route('/search')
def search():
    if not session.get('is_logged_in'):
        return redirect(url_for('login'))
    with connect(g.uuid) as conn:
        cursor = conn.execute("SELECT name,location,description from targets")
        targets = cursor.fetchall()
    return render_template('search.html',targets=targets)

@app.route('/filter', methods=["POST"])
def filter():
    if not session.get('is_logged_in'):
        return redirect(url_for('login'))
    with connect(g.uuid) as conn:
        search = request.form['search']
        terms = search.split(" ")
        query = "SELECT name,location,description from targets"
        for term in terms:
            if detect_sqli(term):
                terms.remove(term)
        if terms:
            location_match = " OR ".join(f"name LIKE '%{term}%'" for term in terms)
            name_match = " OR ".join(f"location LIKE '%{term}%'" for term in terms)
            description_match = " OR ".join(f"description LIKE '%{term}%'" for term in terms)
            query += " WHERE " + " OR ".join([location_match,name_match,description_match])
            print(query)
        cursor = conn.execute(query)
        targets = cursor.fetchall()
        targets = list(targets)
    return jsonify(targets)

@app.route('/admin', methods=["GET"])
def admin():
    if not session.get('is_logged_in') or not session.get('admin'):
        return redirect(url_for('login'))
    return jsonify({"flag":FLAG2})
    

if __name__ == '__main__':
    app.run(debug=True)