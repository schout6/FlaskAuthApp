import unittest
from flask import Flask, url_for
from authenticator import app

class TestRegister(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_register_page_status_code(self):
        response = self.app.get('/register')
        self.assertEqual(response.status_code, 200)

    def test_register_form(self):
        response = self.app.get('/register')
        self.assertIn(b'<form method="POST" action="/register">', response.data)

    # Add more test cases for registration as needed

if __name__ == '__main__':
    unittest.main()
