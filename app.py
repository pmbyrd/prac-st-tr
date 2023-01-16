# 
#* import the necessary modules
import os

from flask import Flask, render_template, request, flash, redirect, session, g
# from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.exc import IntegrityError

# !Remember to import the necessary modules from models.py and other files
# from models_stapi

CURR_USER_KEY = "curr_user"

app = Flask(__name__)

# *Intitialized the global config files
# *necessary for deployment if using a host that is not local
app.config['SQLALCHEMY_DATABASE_URI'] = (
    os.environ.get('DATABASE_URL', 'postgresql:///warbler'))

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "it's a secret")
# toolbar = DebugToolbarExtension(app)

# connect_db(app)
@app.route('/')
def root(): 
    """Root route."""
    
    return redirect('/home')

@app.route('/home')
def home():
    """display the home page"""
    
    return render_template('index.html')