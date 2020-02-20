import os
from flask import Flask, render_template, request, url_for, session, redirect
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'karaokean'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
app.config["secret_key"] = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)


@app.route('/')
def index():
    message = session['username']
    # if 'username' in session:
    #     return 'You are logged in as ' + 

    return render_template("index.html", message=message)

@app.route('/loginpage')
def loginpage():
    return render_template("loginpage.html")


@app.route('/login', methods=['POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'name': request.form['username']})

    if login_user:  
        if check_password_hash(login_user['password'], request.form['password']):
            session['username'] = request.form['username']
            return redirect(url_for('index'))

        return 'Invalid username/password combination'

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name': request.form['username']})

        if existing_user is None:
            hashed_value = generate_password_hash(request.form['password']) 
            users.insert({'name' : request.form['username'], 'password' : hashed_value})
            session['username'] = request.form['username']
            return redirect(url_for('login'))
    
        return 'That Username already exists'

    return render_template('register.html')


if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)
