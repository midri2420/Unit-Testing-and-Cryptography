from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import affine_encode
class MyTestCase(TestCase):
    def test_affine_encode_uppercase(self):
        self.assertEqual(affine_encode("HELLOWORLD", 3, 9),"EVQQZXZIQS")
    def test_affine_encode_uppercase_2(self):
        self.assertEqual(affine_encode("HELLOWORLD", 3, 4), "ZQLLUSUDLN")
    def test_affine_encode_uppercase_3(self):
        self.assertEqual(affine_encode("HELLOWORLD", 5, 9), "SDMMBPBQMY")
    def test_affine_encode_lowercase1(self):
        self.assertEqual(affine_encode("helloworld",3,9), "EVQQZXZIQS")
    def test_affine_encode_empty_insert(self):
        self.assertEqual(affine_encode("", 3, 9 ), "")