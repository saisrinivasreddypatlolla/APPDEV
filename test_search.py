import unittest
from search import *
from models import *

class TestSearch(unittest.TestCase):
    def test_Title(self):
        book = search("Title","Vanishing Acts")
        self.assertEqual(book[0][0].title, "Vanishing Acts")

    def test_Isbn(self):
        book = search("ISBN","055358359X")
        self.assertEqual(book[0][0].isbn,'055358359X')

    def test_Author(self):
        book = search("Author","Tami Hoag")
        self.assertEqual(book[0][0].author,'Tami Hoag')

    def test_provide_Input(self):
        book = search("Author","")
        self.assertEqual(book[1],'Please give input for the search!')

    def test_No_Matching_Results(self):
        book = search("Author","564889231")
        self.assertEqual(book[1],'No Matching results found!')

if __name__ == '__main__':
    unittest.main()