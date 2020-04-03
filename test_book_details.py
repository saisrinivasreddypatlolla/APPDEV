import unittest
from book_details import *
from models import *

class TestSearch(unittest.TestCase):

    def test_book_title(self):
        tok = book_detail("isbn=0142000655")
        #([East of Eden  , East], '')
        result = 'East of Eden'
        self.assertEqual(tok.title.strip(), result)

    def test_book_title_not_found(self):
        tok = book_detail("isbn=014200")
        #([East of Eden  , East], '')
        result = 'Book Not Found'
        self.assertEqual(tok.strip(), result)
if __name__ == '__main__':
    unittest.main()