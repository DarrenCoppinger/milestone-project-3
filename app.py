import os
import re
import math
from flask import Flask, render_template, request, url_for, session, redirect
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
    all_tracks = mongo.db.tracks
    tracks = all_tracks.find().sort('likes', pymongo.DESCENDING).skip(0).limit(5)
    return render_template("index.html", tracks=tracks)


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
                {'name': request.form['username'], 'password': hashed_value, 'playlist': [], 'playlist_name': []})
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
                'lyrics': request.form.get('lyrics_link'),
                'video': youtube_regex_match[6],
                'likes': int(0),
                'dislikes': int(0)
            }
        )

        return redirect(url_for('catalogue'))

    except pymongo.errors.DuplicateKeyError:

        return redirect('addtrack')


@app.route('/edittrack/<track_id>/<page>/<sorting_order>')
def edittrack(track_id, page, sorting_order):
    the_track = mongo.db.tracks.find_one({"_id": ObjectId(track_id)})
    return render_template('edittrack.html', track=the_track, page=page, sorting_order=sorting_order)


@app.route('/update_track/<track_id>/<page>/<sorting_order>', methods=['POST'])
def update_track(track_id, page, sorting_order):
    tracks = mongo.db.tracks
    video = request.form.get('video_link')
    youtube_regex = (
        r'(https?://)?(www\.)?'
        '(youtube|youtu|youtube-nocookie)\.(com|be)/'
        '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')

    youtube_regex_match = re.match(youtube_regex, video)

    likes = request.values.get("likes")
    dislikes = request.values.get("dislikes")

    tracks.update({'_id': ObjectId(track_id)},
                  {
        'name': request.form.get('track_name'),
        'artist': request.form.get('artist_name'),
        'year': int(request.form.get('year')),
        'genre': request.form.get('genre_name'),
        'lyrics': request.form.get('lyrics_link'),
        'video': youtube_regex_match[6],
        'likes': likes,
        'dislikes': dislikes
    })
    return redirect(url_for('catalogue', page=page, sorting_order=sorting_order))


@app.route('/delete_track/<track_id>/<page>/<sorting_order>')
def delete_track(track_id, page, sorting_order):
    mongo.db.tracks.remove( {'_id': ObjectId(track_id)})
    return redirect(url_for('catalogue', page=page, sorting_order=sorting_order))


@app.route('/genre')
def genres():
    """ Template to see existing genres in database"""
    genres = mongo.db.genre.find()
    return render_template('genres.html', genres=genres)


@app.route('/addgenre')
def addgenre():
    """ Template to add new genre to database"""
    return render_template('addgenre.html')


@app.route('/insert_genre', methods=['POST'])
def insert_genre():
    """ Insert new genre to database"""
    genres = mongo.db.genre

    try:
        genres.insert_one(
            {
                'genre': request.form.get('genre_name'),
            }
        )

        return redirect(url_for('genres'))

    except pymongo.errors.DuplicateKeyError:

        return redirect(url_for('genres'))


@app.route('/editgenre/<genre_id>')
def edittrack(genre_id):
    the_genre = mongo.db.genres.find_one({"_id": ObjectId(genre_id)})
    return render_template('editgenre.html')

@app.route('/catalogue')
def catalogue():
    all_tracks = mongo.db.tracks
    tracks_total = all_tracks.count()
    # tracks = all_tracks.find()
    # arg variables
    args = request.args.get

    page_args = int(args("page")) if args(
        "page") else 0  # page_args are initial set to 0
    sorting_order = int(args("sorting_order")) if args("sorting_order") else 1
    print('sorting_order=' + str(sorting_order))
    limit_args = 5

    all_track_count = (range(1, (math.ceil(tracks_total / limit_args)) + 1))

    all_track_pages = []
    all_track_page_args = []

    for page in all_track_count:
        all_track_pages.append(page)
        p_args = (page*limit_args)-limit_args
        all_track_page_args.append(p_args)

    # starting_id = all_tracks.find().sort('_id', pymongo.ASCENDING)
    # last_id = starting_id[page_args]['_id']

    # ---------- SORTING ORDER ----------

    if sorting_order == 2:
        # Date added Oldest Tracks
        ##starting_id = all_tracks.find().sort('_id', pymongo.DESCENDING)
        ##last_id = starting_id[page_args]['_id']
        ##tracks = all_tracks.find({'_id': {'$lte': last_id}}).sort('_id', pymongo.DESCENDING).limit(limit_args)
        tracks = all_tracks.find().sort(
            '_id', pymongo.DESCENDING).skip(page_args).limit(limit_args)

    elif sorting_order == 3:
        # Most Liked Tracks
        ##starting_id = all_tracks.find().sort('likes', pymongo.ASCENDING)
        ##print('starting like'+ str(starting_id))
        ##last_id = starting_id[page_args]['likes']
        ##print('last like'+ str(last_id))
        ##tracks = all_tracks.find({'likes': {'$gte': last_id}}).sort('likes', pymongo.ASCENDING).limit(limit_args)
        tracks = all_tracks.find().sort(
            'likes', pymongo.DESCENDING).skip(page_args).limit(limit_args)
    elif sorting_order == 4:
        # Most Disliked Tracks
        starting_id = all_tracks.find().sort('dislikes', pymongo.ASCENDING)
        last_id = starting_id[page_args]['dislikes']
        tracks = all_tracks.find({'dislikes': {'$gte': last_id}}).sort(
            'dislikes', pymongo.DESCENDING).limit(limit_args)
    else:
        # Date added Newest Tracks
        ##starting_id = all_tracks.find().sort('_id', pymongo.ASCENDING)
        ##last_id = starting_id[page_args]['_id']
        # tracks = all_tracks.find({'_id': {'$gte': last_id}}).limit(limit_args)
        # tracks = all_tracks.find({'_id': {'$gte': last_id}}).limit(limit_args)
        ##tracks = all_tracks.find({'_id': {'$gte': last_id}}).sort('_id', pymongo.ASCENDING).limit(limit_args)
        tracks = all_tracks.find().sort(
            '_id', pymongo.ASCENDING).skip(page_args).limit(limit_args)

    prev_url = page_args - limit_args
    next_url = page_args + limit_args

    return render_template('catalogue.html', tracks=tracks, tracks_total=tracks_total, page=page_args, prev_url=prev_url, next_url=next_url, all_track_pages_id=zip(all_track_pages, all_track_page_args), sorting_order=sorting_order)


@app.route('/sort_by_newest')
def sort_by_newest():
    """ Change sort order of Tracks on catalogue page to ASCENDING date added """
    sorting_order = 1
    return redirect(url_for('catalogue', sorting_order=sorting_order))


@app.route('/sort_by_oldest')
def sort_by_oldest():
    """ Change sort order of Tracks on catalogue page to DESCENDING date added """
    sorting_order = 2
    return redirect(url_for('catalogue', sorting_order=sorting_order))


@app.route('/sort_by_likes')
def sort_by_likes():
    """ Change sort order of Tracks on catalogue page to ASCENDING Likes """
    sorting_order = 3
    return redirect(url_for('catalogue', sorting_order=sorting_order))


@app.route('/sort_by_dislikes')
def sort_by_dislikes():
    """ Change sort order of Tracks on catalogue page to ASCENDING Dislikes """
    sorting_order = 4
    return redirect(url_for('catalogue', sorting_order=sorting_order))


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


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/like/<track_id>', methods=['POST'])
def like(track_id):
    tracks = mongo.db.tracks
    # the_track = mongo.db.tracks.find_one({"_id": ObjectId(track_id)})
    # likes = the_track["likes"]
    # print('likes=' + str(likes))
    # tracks.update(
    #     {"_id": ObjectId(track_id)}, {"$inc": {'likes': 1}})
    tracks.find_one_and_update(
        {"_id": ObjectId(track_id)}, {"$inc": {'likes': 1}})

    return redirect(url_for('catalogue'))


@app.route('/dislike/<track_id>', methods=['POST'])
def dislike(track_id):
    tracks = mongo.db.tracks
    the_track = mongo.db.tracks.find_one({"_id": ObjectId(track_id)})
    dislikes = the_track["dislikes"]
    tracks.find_one_and_update({"_id": ObjectId(track_id)}, {
                               "$inc": {'dislikes': 1}})

    return redirect(url_for('catalogue'))


if __name__ == '__main__':
    app.secret_key = 'secret_key'
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
