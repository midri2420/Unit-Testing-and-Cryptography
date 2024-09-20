from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import affine_decode
class MyTestCase(TestCase):
    def test_affine_decode_uppercase(self):
        self.assertEqual(affine_decode("EVQQZXZIQS", 3, 9),"HELLOWORLD")
    def test_affine_decode_uppercase_2(self):
        self.assertEqual(affine_decode("ZQLLUSUDLN", 3, 4), "HELLOWORLD")
    def test_affine_decode_uppercase_3(self):
        self.assertEqual(affine_decode("SDMMBPBQMY", 5, 9), "HELLOWORLD")
    def test_affine_decode_lowercase1(self):
        self.assertEqual(affine_decode("evqqzxziqs",3,9), "HELLOWORLD")
    def test_affine_decode_empty_insert(self):
        self.assertEqual(affine_decode("", 3, 9 ), "")