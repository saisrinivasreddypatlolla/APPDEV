"""users details file"""
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()
"""
user class
"""
class User(DB.Model):
    __tablename__ = "users"
    username = DB.Column(DB.String(64), primary_key=True, unique=True, nullable=False)
    password = DB.Column(DB.String(128), nullable=False)
    timestamp = DB.Column(DB.DateTime, index=False, unique=False, nullable=False)

    """docstring for User"""
    def __init__(self, username, password, timestamp):
        self.username = username
        self.password = password
        self.timestamp = timestamp

'''
Class for storing book details
'''
class Book(DB.Model):
    __tablename__ = "books"
    # id = DB.Column(DB.Integer, primary_key=True)
    isbn = DB.Column(DB.String(80), primary_key=True, unique=True, nullable=False)
    title = DB.Column(DB.String(80), index=True, unique=False, nullable=False)
    author = DB.Column(DB.String(128))
    year = DB.Column(DB.Integer, index=False, unique=False, nullable=False)

    def __init__(self, isbn, title, author, year) :
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return self.title
