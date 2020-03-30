"""
importing data from books.csv to postgresql
"""
import os, csv
from flask import Flask, render_template, request
from models import *

APP = Flask(__name__)

APP.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
APP.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

DB.init_app(APP)
"""
main method to create table and insert data.
"""
def main():
	#to create the table.
    DB.create_all()
    #reading the file and insertion data into database.
    with open("books.csv", 'r') as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            newBook = Book(row[0], row[1], row[2], int(row[3]))
            DB.session.add(newBook)
    DB.session.commit()

if __name__ == "__main__":
  with APP.app_context():
      main()
