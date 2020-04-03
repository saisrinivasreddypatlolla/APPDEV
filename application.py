"""
This file is used to run the flask
"""
import os
import datetime
<<<<<<< HEAD
from flask import Flask, session, request, render_template, redirect,jsonify
=======
from flask import Flask, session, request, render_template, redirect, jsonify
>>>>>>> master
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from flask_session import Session
from models import *
<<<<<<< HEAD
from search import *
=======
import book_details
import json
>>>>>>> master

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
        try:
            new_user = User(username=user_name, password=password, timestamp=timestamp)
            SESSION.add(new_user)
            SESSION.commit()
            return render_template("registration.html", data="Registered successfully, Please Login")

        except SQLAlchemyError as exception:
            return render_template("registration.html",text="User already exists")
    return render_template('registration.html')
"""
this method is used to show the details of users
to admin.
"""
@APP.route("/admin", methods=["GET"])
def fetch_users():
    print("Method in Admin API: ",request.method)
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

@APP.route("/api/search",methods=['POST'])
def api_search():
    if request.is_json:
        tokens = request.get_json()
        searchType = tokens["type"].strip()
        if "type" in tokens and "search" in tokens and searchType in ['ISBN','Title','Author']:
            searchQuery = tokens['search'].strip()
            results,message = search(searchType,searchQuery)
            if len(message)==0:
                lis = []
                for result in results:
                    b = {}
                    b["ISBN"] = result.isbn
                    lis.append(b)
                resultJson = {}
                resultJson['Books'] = lis
                return jsonify(resultJson)
            return (jsonify({"Error":message}),400)
        return (jsonify({"Error":"Invaiid Request"}),400)
    else:
        return (jsonify({"Error":"Invaiid Request"}),400)

@APP.route("/convert", methods=["POST"])
  def convert():

      # Query for currency exchange rate
      currency = request.form.get("currency")
      res = requests.get("https://api.fixer.io/latest", params={
          "base": "USD", "symbols": currency})

      # Make sure request succeeded
      if res.status_code != 200:
          return jsonify({"success": False})

      # Make sure currency is in response
      data = res.json()
      if currency not in data["rates"]:
          return jsonify({"success": False})

      return jsonify({"success": True, "rate": data["rates"][currency]})

@APP.route("/home", methods = ["GET", "POST"])
def home():
    try:
        text = "Welcome to homepage "+session.get("username")
        if request.method == 'GET':
            searchType = ['ISBN', 'Title', 'Auther']
            try:
                return render_template("userhome.html", text=text,searchType = searchType)
            except:
                return render_template("registration.html", text="Please enter valid username and password")
        else:
            results,message = search(request.form["searchType"],request.form["search"])
            return render_template('userhome.html',books = results,message = message)
    except:
        return render_template("registration.html", text="Please Login")

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

@APP.route("/api/book/<isbn>")
def flight_api(isbn):
    book = book_details.book_detail(isbn)
    if book is None:
        return jsonify({"error": "Invalid book_id"}), 422

    return jsonify({
            "title": book.title,
            "isbn": book.isbn,
            "Author": book.author,
            "Year of Publication": book.year,
        })