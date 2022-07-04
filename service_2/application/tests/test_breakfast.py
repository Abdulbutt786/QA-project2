from application import app
from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch
import application.routes

class TestBase(TestCase):
    def create_app(self):
        return app

class TestDrivers(TestBase):
    @patch('application.routes.random.choice', return_value='Bread and eggs')
    def test_get_breakfast_1(self, patched):
        response =self.client.get(url_for('breakfast'))
        self.assert200(response)
        self.assertIn(b'Bread and eggs', response.data)

    @patch('application.routes.random.choice', return_value='French Toast')
    def test_get_breakfast_2(self, patched):
        response =self.client.get(url_for('breakfast'))
        self.assert200(response)
        self.assertIn(b'French Toast', response.data)

    @patch('application.routes.random.choice', return_value='Pancakes')
    def test_get_breakfast_3(self, patched):
        response =self.client.get(url_for('breakfast'))
        self.assert200(response)
        self.assertIn(b'Pancakes', response.data)

