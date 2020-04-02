import unittest
from models import *
import os
import logging
from flask import Flask, session, request, render_template, redirect, url_for
from flask_session import Session
from sqlalchemy import create_engine, exc, desc, or_
from sqlalchemy.orm import scoped_session, sessionmaker
from datetime import datetime
# from passlib.hash import bcrypt
from application import APP

class BasicTests(unittest.TestCase):
 
    ############################
    #### setup and teardown ####
    ############################
 
    # executed prior to each test
    def setUp(self):
        APP.config['TESTING'] = True
        APP.config['WTF_CSRF_ENABLED'] = False
        APP.config['DEBUG'] = False

        # Check for environment variable
        if not os.getenv("DATABASE_URL"):
            raise RuntimeError("DATABASE_URL is not set")
        # Base.query = db_session.query_property()
        self.APP = APP.test_client()
        self.assertEqual(APP.debug, False)
 
    # executed after each test
    def tearDown(self):
        pass
 
    ########################
    #### helper methods ####
    ########################
     
    def register(self, username, password):
        return self.APP.post('/register',data=dict(username=username, password=password),follow_redirects=True)
     
    def login(self, username, password):
        return self.APP.post('/auth',data=dict(username=username, password=password),follow_redirects=True)
    
 
###############
#### tests ####
###############
 
    def test_register(self):
        response = self.APP.get('/register', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_invalid_user_register(self):
        response = self.register('srinivas', 'password')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'User already exists', response.data)

    def test_invalid_user_login(self):
        response = self.login('srinivas', 'pass')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Please enter valid username and password', response.data)

   

if __name__ == "__main__":
    unittest.main()