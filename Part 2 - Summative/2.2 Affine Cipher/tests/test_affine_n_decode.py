from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import affine_n_decode
class MyTestCase(TestCase):
    def test_affine_n_encode_uppercase(self):
        self.assertEqual(affine_n_decode("XURYWT", 3, 3, 121),"COOLXX")
    def test_affine_n_encode_uppercase2(self):
        self.assertEqual(affine_n_decode("MRHYVS", 3, 3, 121), "HELLOX")
    def test_affine_n_encode_uppercase3(self):
        self.assertEqual(affine_n_decode("KLPWJDVGEZVDSQQWRLMURXSMOEVZMHFLZLQXFWTT", 5, 3, 1721), "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOGXXXX")