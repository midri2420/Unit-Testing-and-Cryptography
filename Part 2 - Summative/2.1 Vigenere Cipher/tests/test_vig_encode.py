from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import vig_encode
class MyTestCase(TestCase):
    def test_vig_encode_uppercase(self):
        self.assertEqual(vig_encode("THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG", "TEST"),"MLWJNMUDUVGPGJGQCYEIXHGOXVLAXPSSRHGZ")
    def test_vig_encode_lowercase1(self):
        self.assertEqual(vig_encode("thequickbrownfoxjumpedoverthelazydog", "test"), "MLWJNMUDUVGPGJGQCYEIXHGOXVLAXPSSRHGZ")
    def test_vig_encode_lowercase2(self):
        self.assertEqual(vig_encode("thequickbrownfoxjumpedoverthelazydog", "TEST"), "MLWJNMUDUVGPGJGQCYEIXHGOXVLAXPSSRHGZ")
    def test_vig_encode_lowercase3(self):
        self.assertEqual(vig_encode("THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG", "test"), "MLWJNMUDUVGPGJGQCYEIXHGOXVLAXPSSRHGZ")
    def test_vig_encode_empty_insert(self):
        self.assertEqual(vig_encode("", "TEST" ), "")
    def test_vig_encode_empty_insert2(self):
        self.assertEqual(vig_encode("THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG", ""), "")