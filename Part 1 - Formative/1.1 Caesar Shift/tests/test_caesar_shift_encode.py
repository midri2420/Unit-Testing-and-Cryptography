from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import caesar_encode
class MyTestCase(TestCase):
    def test_caesar_encode_uppercase(self):
        self.assertEqual(caesar_encode("HELLOWORLD", 5), "MJQQTBTWQI")  # add assertion here
    def test_caesar_encode_lowercase(self):
        self.assertEqual(caesar_encode("helloworld", 5), "MJQQTBTWQI")
    def test_caesar_encode_empty_insert(self):
        self.assertEqual(caesar_encode("", 5), "")
