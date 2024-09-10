from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import sub_encode
class MyTestCase(TestCase):
    def test_sub_decode_uppercase(self):
        self.assertEqual(sub_encode("HELLOWORLD", "WJKUXVBMIYDTPLHZGONCRSAEFQ"),"MXTTHAHOTU") # add assertion here
    def test_sub_decode_lowercase(self):
        self.assertEqual(sub_encode("helloworld", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "MXTTHAHOTU")
    def test_sub_decode_empty_insert(self):
        self.assertEqual(sub_encode("", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "")