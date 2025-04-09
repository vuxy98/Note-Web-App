#DATABASE MODEL
from website import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))#the reason why user here isn't User bcuz Python class must starts with uppercase, though in database, its lowercase, like yk, user not User
#u can use user.id, email, or whatever u want, tho this foreign key should only be used for one to many relationships(1 user has many notes)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')#everytime user create a note, add into the user's note relationship that note id
