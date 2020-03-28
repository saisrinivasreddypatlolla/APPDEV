import os
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from flask import Flask, session, request, flash
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import render_template
from sqlalchemy.exc import SQLAlchemyError
from models import *;
import datetime

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
session=db()
@app.route("/")
def index():
    return "Project 1: TODO"

@app.route("/register",methods=['GET','POST'])
def register():
    # # form = request.form
    if request.method == "POST":
        user_name=request.form['username']
        password = request.form['password']
        timestamp = datetime.datetime.now()
        # print(timestamp)
        try:
            new_user = User(username= user_name, password = password, timestamp = timestamp) 
            session.add(new_user)
            session.commit()
            return "<h2>Registered successfully, Please Login</h2>"

        except SQLAlchemyError as e:
            message = str(e.__dict__['orig'])
            return "<h2>message</h2>"
    return render_template('registration.html')

@app.route("/admin", methods=["GET"])
def fetch_users():
    users = session.query(User).all()
    # print(user?)
    return render_template('admin.html', users=users)
