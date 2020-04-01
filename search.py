import os
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from models import *

# Set up database
ENGINE = create_engine(os.getenv("DATABASE_URL"))
DB = scoped_session(sessionmaker(bind=ENGINE))
SESSION = DB()

def search(typeOfSearch,searchedFor):
    books = []
    message = ""
    if(len(searchedFor)>0):
        if typeOfSearch == 'ISBN':
            books = SESSION.query(Book).filter(Book.isbn.like(f'%{searchedFor}%')).all()
        elif typeOfSearch == 'Title':
            books = SESSION.query(Book).filter(Book.title.like(f'%{searchedFor}%')).all()
        elif typeOfSearch == 'Author':
            books = SESSION.query(Book).filter(Book.author.like(f'%{searchedFor}%')).all()
        if len(books)== 0:
            message = "No Matching results found!"
        return books,message
    else:
        message = "Please give input for the search!"
        return books,message

def main():
    tok = input().split(" ")
    typeOfSearch = tok[0]
    searchedFor = tok[1]
    print(search(typeOfSearch,searchedFor))

if __name__ == "__main__":
      main()