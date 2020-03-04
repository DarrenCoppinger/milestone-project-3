import os
import re
from flask import Flask, render_template, request, url_for, session, redirect, jsonify
from flask_pymongo import PyMongo, pymongo
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
    # if 'username' in session:
    #     message = session['username']
    #     return render_template("index.html", message=message)
    return render_template("index.html") 


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
            """ Add empty list called playlist """
            return redirect(url_for('index'))

        return 'Invalid username/password combination'


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name': request.form['username']})

        if existing_user is None:
            hashed_value = generate_password_hash(request.form['password'])
            users.insert(
                {'name': request.form['username'], 'password': hashed_value, 'playlist': [], 'playlist_name': [] })
            session['username'] = request.form['username']
            return redirect(url_for('index'))

        return 'That Username already exists'

    return render_template('register.html')


@app.route('/addtrack')
def addtrack():
    return render_template('addtrack.html')


@app.route('/insert_track', methods=['POST'])
def insert_track():
    tracks = mongo.db.tracks
    video = request.form.get('video_link')
    youtube_regex = (
        r'(https?://)?(www\.)?'
        '(youtube|youtu|youtube-nocookie)\.(com|be)/'
        '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')

    youtube_regex_match = re.match(youtube_regex, video)
    print(youtube_regex_match)
    print(youtube_regex_match[6])

    try:
        tracks.insert_one(
            {
                'name': request.form.get('track_name'),
                'artist': request.form.get('artist_name'),
                'year': int(request.form.get('year')),
                'genre': request.form.get('genre_name'),
                'lyrics': request.form.get('youtube_link'),
                'video': youtube_regex_match[6],
                'likes': 0,
                'dislikes': 0
            }
        )
        
        return redirect(url_for('index'))

    except pymongo.errors.DuplicateKeyError:

        return redirect('addtrack')

@app.route('/catalogue')
def catalogue():
    tracks = mongo.db.tracks.find()
    all_tracks = mongo.db.tracks
    tracks_total = all_tracks.count()
    return render_template('catalogue.html', tracks=tracks, tracks_total=tracks_total)


@app.route('/playlist_page')
def playlist_page():
    """ Show Users Playlist"""
    users = mongo.db.users
    username = session['username']
    the_user = users.find_one({"name": username})
    playlist_ids = []
    playlist_names = []
    for ytv in the_user["playlist"]:
        playlist_ids.append(ytv)
    for pl_name in the_user["playlist_name"]:
        playlist_names.append(pl_name)
    # tracks = mongo.db.tracks.find()
    # pl = the_user.playlist
    # the_track = mongo.db.tracks.find_one({"video": pl})

    return render_template('playlist_page.html', users=the_user, playlist=zip(playlist_ids, playlist_names))


@app.route('/playlist_addto/<track_id>', methods=['POST'])
def playlist_addto(track_id):
    """ Add the youtube_id of a video link to a list called playlist"""
    users = mongo.db.users
    username = session['username']

    the_track = mongo.db.tracks.find_one({"_id": ObjectId(track_id)})
    ytv = the_track["video"]
    pl_name = the_track["name"]

    users.find_one_and_update(
        {"name": username}, {"$push": {'playlist': ytv, 'playlist_name': pl_name}})

    return redirect(url_for('catalogue'))


@app.route('/playlist_delete/<track_id>', methods=['POST'])
def playlist_delete(track_id):
    """ Delete the _id of a video link from the array playlist in the database"""
    users = mongo.db.users
    username = session['username']
    users.find_one_and_update({"name": username},
        {"$pull": {'playlist': track_id}})
    return redirect(url_for('catalogue'))


if __name__ == '__main__':
    app.secret_key = 'secret_key'
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
