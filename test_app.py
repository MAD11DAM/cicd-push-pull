import unittest
from app import version

class TestApp(unittest.TestCase):
    def test_version(self):
        self.assertEqual(version(), '1.0.0')
