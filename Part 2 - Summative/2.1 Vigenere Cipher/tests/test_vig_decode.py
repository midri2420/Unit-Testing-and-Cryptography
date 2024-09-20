from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import vig_decode
class MyTestCase(TestCase):
    def test_vig_decode_uppercase(self):
        self.assertEqual(vig_decode("MLWJNMUDUVGPGJGQCYEIXHGOXVLAXPSSRHGZ", "TEST"),"THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG")
    def test_vig_decode_lowercase1(self):
        self.assertEqual(vig_decode("mlwjnmuduvgpgjgqcyeixhgoxvlaxpssrhgz", "test"), "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG")
    def test_vig_decode_lowercase2(self):
        self.assertEqual(vig_decode("mlwjnmuduvgpgjgqcyeixhgoxvlaxpssrhgz", "TEST"), "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG")
    def test_vig_decode_lowercase3(self):
        self.assertEqual(vig_decode("MLWJNMUDUVGPGJGQCYEIXHGOXVLAXPSSRHGZ", "test"), "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG")
    def test_vig_decode_empty_insert(self):
        self.assertEqual(vig_decode("", "TEST" ), "")
    def test_vig_decode_empty_insert2(self):
        self.assertEqual(vig_decode("MLWJNMUDUVGPGJGQCYEIXHGOXVLAXPSSRHGZ", ""), "")