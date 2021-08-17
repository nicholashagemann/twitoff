from flask import Flask
from flask import render_template
from flask import request
from .models import db, Tweet, User
import os


def create_app():
    #get the path to the app directory
    app_dir = os.path.dirname(os.path.abspath(__file__))

    #location of the database in the app directory
    database = "sqlite:///{}".format(os.path.join(app_dir, "twitoff.sqlite3"))

    app = Flask(__name__)

    #set up database
    app.config["SQLALCHEMY_DATABASE_URI"] = database
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    #create tables
    with app.app_context():
        db.create_all()

    @app.route('/', methods = ["GET", "POST"])
    def home():
        name = request.form.get('name')

        if name:
            user = User(name=name)
            db.session.add(user)
            db.session.commit()
        
        tweet = request.form.get('tweet')

        if tweet:
            tweet = Tweet(text=tweet)
            db.session.add(user)
            db.session.add(tweet)
            db.session.commit()

        users = User.query.all()
        return render_template('home.html', users=users)
    
    return app
