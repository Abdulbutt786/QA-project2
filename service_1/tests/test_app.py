from flask import Flask, url_for
from flask_testing import TestCase
import application.routes
from application import app 
from unittest.mock import patch
import requests_mock

class TestBase(TestCase):
    def create_app(self):
        return app

#Testing the route index
class Testindex(TestBase):
    def test_get_index(self):
            response =self.client.get(url_for('index'))
            self.assert500(response)

#Test meal 
class Testmeal1(TestBase):
    def test_meal1(self):
        with requests_mock.Mocker() as m:
            m.get('http://service2:5000/get_breakfast', text='Bread and eggs')
            m.get('http://service3:5000/get_lunch', text='Veg Pizza')
            m.post('http://service4:5000/calories', text='70')
            
            response =self.client.get(url_for('index'))
            self.assert200(response)
            self.assertIn(b'Bread and eggs', response.data)
            self.assertIn(b'Veg Pizza', response.data)
            self.assertIn(b'', response.data)

#Test meal 2
    def test_meal2(self):
        with requests_mock.Mocker() as m:
            m.get('http://service2:5000/get_breakfast', text='French Toast')
            m.get('http://service3:5000/get_lunch', text='Chicken and chips')
            m.post('http://service4:5000/calories', text='')
            
            response =self.client.get(url_for('index'))
            self.assert200(response)
            self.assertIn(b'French Toast', response.data)
            self.assertIn(b'Chicken and chips', response.data)
            self.assertIn(b'', response.data)

#Test meal 2
    def test_meal3(self):
        with requests_mock.Mocker() as m:
            m.get('http://service2:5000/get_breakfast', text='French Toast')
            m.get('http://service3:5000/get_lunch', text='Chicken and chips')
            m.post('http://service4:5000/calories', text='')
            
            response =self.client.get(url_for('index'))
            self.assert200(response)
            self.assertIn(b'French Toast', response.data)
            self.assertIn(b'Chicken and chips', response.data)
            self.assertIn(b'', response.data)