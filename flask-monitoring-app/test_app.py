import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from app import app  # Now Python should find app.py correctly

import unittest

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Flask Monitoring App is Running.", response.data)

    def test_health_check(self):
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'"status":"healthy"', response.data)

if __name__ == '__main__':
    unittest.main()