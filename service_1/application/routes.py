from application import app
from flask import render_template
import requests

@app.route('/')
@app.route('/home')
def index():
	return render_template('index.html')

@app.route('/generate')
def index():
    breakfast = requests.get('http://service2:5000/get_breakfast').text
    lunch = requests.get('http://service3:5000/get_lunch').text
    price = requests.post('http://service4:5000/price', json=dict(chars=chars, nums=nums))
    return render_template('home.html', prize = prize.text)