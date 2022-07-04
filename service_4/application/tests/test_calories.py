from application import app
from flask import url_for
from flask_testing import TestCase
import requests_mock


class TestBase(TestCase):
    def create_app(self):
        return app


class Testcalories(TestBase):
    def test_get_calories1(self):
        response = self.client.post(url_for('calories_gen'), json={"breakfasts": "Bread and eggs", "lunches": "Veg Pizza"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'250', response.data)

    def test_get_calories2(self):
        response = self.client.post(url_for('calories_gen'), json={"breakfasts": "French Toast", "lunches": "Chicken and chips"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'230', response.data)


    def test_get_calories3(self):
        response = self.client.post(url_for('calories_gen'), json={"breakfasts": "Nuts and Seeds Granola", "lunches": "Burger and Chips"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'300', response.data)
    
    def test_get_calories4(self):
        response = self.client.post(url_for('calories_gen'), json={"breakfasts": "Norwegian Risgrøt Rice Porridge", "lunches": "Pasta"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'196', response.data)
    
    def test_get_calories5(self):
        response = self.client.post(url_for('calories_gen'), json={"breakfasts": "Pancakes", "lunches": "Lentil soup"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'168', response.data)
     
    def test_get_calories6(self):
        response = self.client.post(url_for('calories_gen'), json={"breakfasts": "Waffles with stawberries", "lunches": "Mac and Cheese"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'336', response.data)
    
    def test_get_calories7(self):
        response = self.client.post(url_for('calories_gen'), json={"breakfasts": "Cheesy skillet hash brown & eggs", "lunches": "Beef burger"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'193', response.data)


