import unittest
from flask import Flask, url_for
from authenticator import app

class TestLogin(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_login_page_status_code(self):
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200)

    def test_login_form(self):
        response = self.app.get('/login')
        self.assertIn(b'<form method="POST" action="/login">', response.data)

    # Add more test cases for login as needed

if __name__ == '__main__':
    unittest.main()
