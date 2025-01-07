from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True) # create id for each object(automatically increments id-> 001, 002...)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone = True), default=func.now()) # get current date and time for note object
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # set up relationship between the user and note

class Reminder():
    #TBD
    pass


# set up user model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique=True) # 150 = maximum length
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')