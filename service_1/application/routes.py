from application import app
from flask import render_template
from application import app, db
import requests
from application.models import Meal

@app.route('/')
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/')
def home():
    breakfast = requests.get('http://service2:5000/get/breakfast')
    lunch = requests.get('http://service3:5000/get/lunch', data=breakfast.text)
    price = requests.post('http://service4:5000/calories',data=lunch.txt )


    return render_template('home.html', breakfast=