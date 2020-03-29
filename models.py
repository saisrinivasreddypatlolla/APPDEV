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
