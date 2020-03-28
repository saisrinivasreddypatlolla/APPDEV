import os
from flask import Flask, render_template, request

#import user table definition
from models import *;

app = Flask(__name__)

#tell flask what SQLAlchemy database to use
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#link flask app with database(we are not running flask yet)
db.init_app(app)

def main():
	#create tables based on each table definition in "models"
	db.create_all()

if __name__ == '__main__':
	#allows foe command line interactions with flask application
	with app.app_context():
		main()