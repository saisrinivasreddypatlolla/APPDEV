import os
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from flask import Flask, session, request, flash
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import render_template

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    return "Project 1: TODO"

@app.route("/register",methods=['GET','POST'])
def register():
    # # form = request.form
    if request.method == "POST":
        print("Name: ",request.form['username'])
        print("Passowrd: ",request.form['password'])
        return "<h2 text-align=\"center\">Hello "+request.form['username']+", Welcome !</h2>"
    return render_template('registration.html')
