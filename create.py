"""
it is used to create the user table in database
"""
import os
from flask import Flask

#import user table definition
from models import *

APP = Flask(__name__)

#tell flask what SQLAlchemy database to use
APP.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
APP.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#link flask APP with database(we are not running flask yet)
DB.init_app(APP)
"""
main funtion to create table.
"""
def main():
    #create tables based on each table definition in "models"
    DB.create_all()

if __name__ == '__main__':
    #allows foe command line interactions with flask APPlication
    with APP.app_context():
        main()
