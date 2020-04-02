"""
This file is used to run the flask
"""
import os
import datetime
from flask import Flask, session, request, render_template, redirect
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from flask_session import Session
from models import *
import book_details

APP = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
APP.config["SESSION_PERMANENT"] = False
APP.config["SESSION_TYPE"] = "filesystem"
Session(APP)

# Set up database
ENGINE = create_engine(os.getenv("DATABASE_URL"))
DB = scoped_session(sessionmaker(bind=ENGINE))
SESSION = DB()
"""
index method is used when we start our app.
"""
@APP.route("/")
def index():
    if session.get("username") is None:
        return render_template('registration.html', text="Please Login")
    return render_template('userhome.html', text="Welcome to homepage "+session.get("username"))
"""
register method is used to take data from
user and store in database.
"""
@APP.route("/register", methods=['GET', 'POST'])
def register():
    # # form = request.form
    if request.method == "POST":
        user_name = request.form['username']
        password = request.form['password']
        timestamp = datetime.datetime.now()
        # print(timestamp)
        try:
            new_user = User(username=user_name, password=password, timestamp=timestamp)
            SESSION.add(new_user)
            SESSION.commit()
            return render_template("registration.html", data="Registered successfully, Please Login")

        except SQLAlchemyError as exception:
            return exception
    return render_template('registration.html')
"""
this method is used to show the details of users
to admin.
"""
@APP.route("/admin", methods=["GET"])
def fetch_users():
    users = SESSION.query(User).all()
    # print(user?)
    return render_template('admin.html', users=users)
"""
this method is used for the authentication
of user when the person clicks login button.
"""
@APP.route("/auth", methods=["POST"])
def authentication():
    username = request.form["username"]
    password = request.form["password"]
    data = SESSION.query(User).filter_by(username=username)
    # print(data)
    try:
        if data[0].username == username and data[0].password == password:
            session["username"] = data[0].username
            return redirect("/home")
    except:
        return render_template("registration.html", text="Please enter valid username and password")
    return render_template("registration.html", text="Please enter valid username and password")

@APP.route("/home", methods = ["GET", "POST"])
def home():
    try:
        return render_template("userhome.html", text="Welcome to homepage "+session.get("username"))
    except:
        return render_template("registration.html", text="Please enter valid username and password")
"""
this method used when the user clicks logout button.
"""
@APP.route("/logout")
def logout():
    session.clear()
    return render_template("registration.html", text="successfully logged out")

@APP.route("/book/<string:arg>")
def details(arg):
    if session.get("username") is None:
        return render_template('registration.html', text="Please Login")
    result = book_details.book_detail(arg)
    # isbn = arg.strip().split("=")[1]
    # # book = request.args.get(isbn)
    # data = SESSION.query(Book).filter_by(isbn=isbn)
    if type(result) == str:
        return render_template("report.html",text=result)
    return render_template("bookdetails.html",data=result)
