# Run by Docker
# This file is included to reduce the guessiness of this challenge. 
# The file run is main.py, which is the identical as the file here.

from flask import Flask, request, render_template , redirect, url_for,render_template_string
import os 
app = Flask(__name__)
FLAG = open('flag.txt').read()

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/view', methods = ["GET"])
def view():
    file_name = request.args.get('file_name')
    if not file_name:
        return redirect(url_for('index'))
    
    file_path = os.path.join(os.getcwd(), file_name)
    
    if not os.path.exists(file_path):
        return render_template('error.html')
    
    with open(file_path, "r") as f:
        content = f.read()
    
    content = content.replace(FLAG, "")

    return render_template("display.html",content = content,file_name = file_name)

if __name__ == '__main__':
    app.run(debug = True)