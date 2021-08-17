from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return "<User: {}>".format(self.name)

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Unicode(300))
    user_id = db.Column(db.Integer, 
                        db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('user', backref=db.backref('tweet', lazy=True))

    def __repr__(self):
        return '<Tweet: {}'.format(self.text)
