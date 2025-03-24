from flask import Flask, request, jsonify, render_template, session, make_response
import uuid
import jwt 
import os 
import re 
import sqlite3
import os 
import random

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'super_secret')
command_responses = {
    "yes": "but no, but yes, ",
    "no": "but yes, but no, ",
    "but": "but but, ",
}
class RandomResponse:
    def __init__(self, response):
        self.response = response
        self.reroll()

    def reroll(self):
        rand_gen = random.randint(1,10)
        self.generated = self.response*rand_gen

def generate_response(response, command):
    responseObj = RandomResponse(response)
    message = "{response.generated} but "+command+"."
    return message.format(response = responseObj)

def save_token(uuid, secret):
    db = sqlite3.connect('secrets.db')
    cursor = db.cursor()
    sql = "INSERT OR IGNORE INTO secrets (uuid, secret) VALUES (?, ?)"
    cursor.execute(sql, (uuid, secret))
    sql = "UPDATE secrets SET secret = ? WHERE uuid = ?"
    cursor.execute(sql, (secret, uuid))
    db.commit()
    db.close()

def get_secret(uuid):
    db = sqlite3.connect('secrets.db')
    db.row_factory = lambda cursor, row: row[0]
    cursor = db.cursor()
    sql = "SELECT secret FROM secrets WHERE uuid = ?"
    cursor.execute(sql, (uuid,))
    secret = str(cursor.fetchone())
    db.close()
    return secret


def generate_jwt_token():
    user_info = {
        "admin":False
    }
    secret = os.urandom(32)
    secret = secret.hex()
    token = jwt.encode(user_info,secret,"HS256")
    return [token,secret]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin', methods=['GET'])
def admin():
    print(request.cookies,session)
    if request.cookies.get('token') is None or session.get('uuid') is None:
        return jsonify({"response": "Unauthorized", "status": 401})
    token = request.cookies.get('token')
    uuid = session['uuid']
    secrets = get_secret(session['uuid'])
    try:
        decoded = jwt.decode(token, secrets, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return jsonify({"response": "Token Expired", "status": 401})
    except jwt.InvalidTokenError:
        return jsonify({"response": "Invalid Token", "status": 401})
    
    if decoded['admin']:
        return jsonify({"response": f"Welcome Admin. Here's the Flag: {os.getenv('FLAG','TESTFLAG{}')}", "status": 200})
    else:
        return jsonify({"response": "Only admin's can access this page!", "status": 401})

@app.route('/api', methods=['POST'])
def api():

    session.setdefault('uuid', str(uuid.uuid4()))
    data = request.get_json()
    command = data.get('command')
    prefix = command.split(" ")[0].lower()

    if prefix not in command_responses:
        return jsonify({"response": "Invalid Command", "status": 400})
    
    response = generate_response(command_responses[prefix], command)

    jwt_token, secret = generate_jwt_token() 
    save_token(session['uuid'], secret)

    response = make_response(jsonify({"response": response, "status": 200}))
    response.set_cookie('token', jwt_token)
    
    return response


if __name__ == '__main__':
    app.run()
