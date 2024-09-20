from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import convert_to_text
class MyTestCase(TestCase):
    def test_convert_to_text_uppercase(self):
        self.assertEqual(convert_to_text(28), "CB")
    def test_convert_to_text_uppercase_2(self):
        self.assertEqual(convert_to_text(53), "BC")
    def test_convert_to_text_uppercase_3(self):
        self.assertEqual(convert_to_text(187253), "BARK")
    def test_convert_to_text_uppercase_4(self):
        self.assertEqual(convert_to_text(218741750267309021256255930435388550208768849997977), "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG")
    def test_convert_to_text_lowercase(self):
        self.assertEqual(convert_to_text(218741750267309021256255930435388550208768849997977), "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG")
    def test_convert_to_text_empty_insert(self):
        self.assertEqual(convert_to_text(0), "")