from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import convert_to_num
class MyTestCase(TestCase):
    def test_convert_to_num_uppercase(self):
        self.assertEqual(convert_to_num("CB"), 28)
    def test_convert_to_num_uppercase_2(self):
        self.assertEqual(convert_to_num("BC"), 53)
    def test_convert_to_num_uppercase_3(self):
        self.assertEqual(convert_to_num("BARK"), 187253)
    def test_convert_to_num_uppercase_4(self):
        self.assertEqual(convert_to_num("THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"), 218741750267309021256255930435388550208768849997977)
    def test_convert_to_num_lowercase(self):
        self.assertEqual(convert_to_num("thequickbrownfoxjumpedoverthelazydog"), 218741750267309021256255930435388550208768849997977)
    def test_convert_to_num_empty_insert(self):
        self.assertEqual(convert_to_num(""), 0)