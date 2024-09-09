from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import sub_encode
class MyTestCase(TestCase):
    def test_caesar_decode_uppercase(self):
        self.assertEqual(sub_encode("MJQQTBTWQI", 5), "HELLOWORLD")  # add assertion here
    def test_caesar_decode_lowercase(self):
        self.assertEqual(sub_encode("mjqqtbtwqi", 5), "HELLOWORLD")
    def test_caesar_decode_empty_insert(self):
        self.assertEqual(sub_encode("", 5), "")