from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import rsa_encode
class MyTestCase(TestCase):
    def test_rsa_encode_1(self):
        self.assertEqual(rsa_encode("THEFIVEBOXINGWIZARDSJUMPQUICKLY", 89791663297454218925122821203164688040223092413375743264939186396302475331561, 65537), 34028226424022141662679340496616735128390579906964150145035108807466384852365)