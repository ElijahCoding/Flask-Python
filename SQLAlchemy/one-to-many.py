from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:root@127.0.0.1:8889/fresh"
db = SQLAlchemy(app)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    pets = db.relationship('Pet', backref='owner') # class

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    owner_id = db.Column(db.Integer, db.ForeignKey('person.id')) # table
