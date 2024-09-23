from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import affine_n_decode
class MyTestCase(TestCase):
    def test_affine_n_encode_uppercase(self):
        self.assertEqual(affine_n_decode("COOL", 3, 3, 121),"XURYWT")
    # def test_affine_n_encode_uppercase2(self):
    #     self.assertEqual(affine_n_encode("HELLO", 4, 5, 1042), "")
    def test_affine_n_encode_uppercase(self):
        self.assertEqual(affine_n_decode("KLPWJDVGEZVDSQQWRLMURXSMOEVZMHFLZLQXFWTT", 5, 3, 1721), "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOGXXXX")