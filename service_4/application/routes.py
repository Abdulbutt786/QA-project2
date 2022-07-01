from flask import Flask
from flask import request
from application import app
import random as rd 

@app.route('/calories', methods=['POST'])
def calories_gen():
    allcalories = 0
    data = request.get_json()
    # breakfast
    if data['breakfasts'] == 'Bread and eggs':
        allcalories += 10
    if data['breakfasts'] == 'French Toast':
        allcalories += 40      
    if data['breakfasts'] == 'Nuts and Seeds Granola':
        allcalories += 50
    if data['breakfasts'] == 'Norwegian Risgrøt Rice Porridge':
        allcalories += 45
    if data['breakfasts'] == 'Cheesy skillet hash brown & eggs':
        allcalories += 25
    if data['breakfasts'] == 'Pancakes':
        allcalories += 30
    if data['breakfasts'] == 'Waffles with stawberries':
        allcalories += 30

    # lunch
    if data['lunches'] == 'Veg Pizza':
        allcalories += 5
    if data['lunches'] == 'Chicken and chips':
        allcalories += 15
    if data['lunches'] == 'Burger and Chips':
        allcalories += 30
    if data['lunches'] == 'Pasta':
        allcalories += 50
    if data['lunches'] == 'Lentil soup':
        allcalories += 100
    if data['lunches'] == 'Mac and Cheese':
        allcalories += 250
    if data['lunches'] == 'Beef burger':
        allcalories += 150

    return str(allcalories)