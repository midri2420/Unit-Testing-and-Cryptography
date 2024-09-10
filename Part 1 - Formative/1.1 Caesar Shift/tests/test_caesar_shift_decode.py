from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import caesar_decode
class MyTestCase(TestCase):
    def test_caesar_decode_uppercase(self):
        self.assertEqual(caesar_decode("MJQQTBTWQI", 5), "HELLOWORLD")  # add assertion here
    def test_caesar_decode_lowercase(self):
        self.assertEqual(caesar_decode("mjqqtbtwqi", 5), "HELLOWORLD")
    def test_caesar_decode_empty_insert(self):
        self.assertEqual(caesar_decode("", 5), "")