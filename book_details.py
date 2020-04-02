import os
# import datetime
from flask import Flask, session, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from models import *

# Set up database
ENGINE = create_engine(os.getenv("DATABASE_URL"))
DB = scoped_session(sessionmaker(bind=ENGINE))
SESSION = DB()

def book_detail(arg):
    isbn = arg.strip().split("=")[1]
    data = SESSION.query(Book).filter_by(isbn=isbn).first()
    if data is None:
    	return "Book Not Found"
    return data
