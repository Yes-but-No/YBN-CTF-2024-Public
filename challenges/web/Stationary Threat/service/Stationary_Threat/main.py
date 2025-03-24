from flask import Flask, request, jsonify,render_template,session
import os
app = Flask(__name__)
app.secret_key = os.urandom(24)
roles = ['user', 'student','admin', 'teacher']
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/users/<_id>/roles', methods=['POST'])
def create_role(_id):
    # Our State of the Art Authentication System
    if 1==1:
        _id = int(_id)
        if _id < 0 or _id > len(roles):
            return jsonify({'message': 'Invalid id'}), 400
        session['role'] = roles[_id]
        return jsonify({'message': 'Role created successfully'})
    else:
        return jsonify({'message': 'Unauthorized'}), 401
    
@app.route('/nuke')
def nuke():
    role = session.get('role',"user")
    if role == 'admin':
        flag = open('flag.txt','r').read()
    else:
        flag = None 
    return render_template('nuke.html', flag=flag)

@app.route('/dashboard')
def dashboard():
    user = session.get('role',"user")
    return render_template('dashboard.html',user=user)

if __name__ == '__main__':
    app.run()