import unittest
from search import *
from models import *
from application import *

class TestApplication(unittest.TestCase):
    def test_get_(self):
        response = redirect('http://127.0.0.1:5000/')
        print("response code: ",response.status_code)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()