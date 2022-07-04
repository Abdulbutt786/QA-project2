from application import app
from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch
import application.routes

class TestBase(TestCase):
    def create_app(self):
        return app

class TestDrivers(TestBase):
    @patch('application.routes.random.choice', return_value='Veg Pizza')
    def test_get_lunch_1(self, patched):
        response =self.client.get(url_for('get_lunch'))
        self.assert200(response)
        self.assertIn(b'Veg Pizza', response.data)

    @patch('application.routes.random.choice', return_value='Chicken and chips')
    def test_get_lunch_2(self, patched):
        response =self.client.get(url_for('get_lunch'))
        self.assert200(response)
        self.assertIn(b'Chicken and chips', response.data)
    
    @patch('application.routes.random.choice', return_value='Lentil soup')
    def test_get_lunch_3(self, patched):
        response =self.client.get(url_for('get_lunch'))
        self.assert200(response)
        self.assertIn(b'Lentil soup', response.data)
    
    @patch('application.routes.random.choice', return_value='Chicken fried rice')
    def test_get_lunch_4(self, patched):
        response =self.client.get(url_for('get_lunch'))
        self.assert200(response)
        self.assertIn(b'Chicken fried rice', response.data)

    @patch('application.routes.random.choice', return_value='Pasta')
    def test_get_lunch_5(self, patched):
        response =self.client.get(url_for('get_lunch'))
        self.assert200(response)
        self.assertIn(b'Pasta', response.data)
    