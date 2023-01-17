from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
db = SQLAlchemy()

def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)
    
# *make a class for actors for the db
class Actor(db.Model):
    """Actor"""
    __tablename__ = "actors"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    f_name = db.Column(db.String(20), nullable=False)
    l_name = db.Column(db.String(20), nullable=False)
    char_name = db.Column(db.String, nullable=False)
    
    # make a method that return the full name of the actor
    def __repr__(self):
        return f"<Actor {self.id} {self.full_name} {self.char_name}>"
    
    @property
    def full_name(self):
        return f"{self.f_name} {self.l_name}"
    
class Character(db.Model):
    """Creates a character table"""
    
    __tablename__ = "characters"
    
    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=False)
    yearOfBirth = db.Column(db.Integer, nullable=False)
    monthOfBirth = db.Column(db.Integer, nullable=False)
    dayOfBirth = db.Column(db.Integer, nullable=False)
    placeOfBirth = db.Column(db.String, nullable=False)
    yearOfBirth = db.Column(db.Integer, nullable=False)
    monthOfDeath = db.Column(db.Integer, nullable=False)
    dayOfDeath = db.Column(db.Integer, nullable=False)
    placeOfDeath = db.Column(db.String, nullable=False)
    height 
    # *make a relationship with the movies table
    # *make a relationship with the shows table
    
    
