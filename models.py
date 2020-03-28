from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
	__tablename__ = "users"
	username = db.Column(db.String(64),
		primary_key = True,
		unique = True,
		nullable=False)
	password = db.Column(db.String(128),
		nullable=False)
	timestamp = db.Column(db.DateTime,
		index=False,
		unique=False,
		nullable=False)

	"""docstring for User"""
	def __init__(self, username,password,timestamp):
		self.username = username
		self.password = password
		self.timestamp = timestamp

		