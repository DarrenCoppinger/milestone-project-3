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

mongo = PyMongo(app)

@app.route('/')
@app.route('/index')
def home():
    return render_template("index.html", categories=mongo.db.categories.find())

@app.route('/<password>')
def 

if __name__ == '__main__':
    app.secret_key = 'mysercet'
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)