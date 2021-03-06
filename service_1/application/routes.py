from application import app
from flask import render_template
import requests

@app.route('/')
def index():
    breakfast = requests.get('http://service2:5000/get_breakfast').text
    lunch = requests.get('http://service3:5000/get_lunch').text
    calories = requests.post('http://service4:5000/calories',json={'breakfasts':breakfast,'lunches':lunch})
    return render_template('home.html', breakfast=breakfast, lunch=lunch, calories=calories.text)