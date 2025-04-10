from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True,nullable = False)
    password = db.Column(db.String(130),nullable=False)


class Car(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(150),nullable = True)
    available = db.Column(db.Boolean,default=True)

class Booking(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    car_id = db.Column(db.Integer,db.ForeignKey('car.id'))