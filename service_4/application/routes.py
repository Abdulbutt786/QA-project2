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
        allcalories += 70
    if data['breakfasts'] == 'French Toast':
        allcalories += 90    
    if data['breakfasts'] == 'Nuts and Seeds Granola':
        allcalories += 90
    if data['breakfasts'] == 'Norwegian Risgrøt Rice Porridge':
        allcalories += 76
    if data['breakfasts'] == 'Cheesy skillet hash brown & eggs':
        allcalories += 73
    if data['breakfasts'] == 'Pancakes':
        allcalories += 98
    if data['breakfasts'] == 'Waffles with stawberries':
        allcalories += 149

    # lunch
    if data['lunches'] == 'Veg Pizza':
        allcalories += 180
    if data['lunches'] == 'Chicken and chips':
        allcalories += 140
    if data['lunches'] == 'Burger and Chips':
        allcalories += 210
    if data['lunches'] == 'Pasta':
        allcalories += 120
    if data['lunches'] == 'Lentil soup':
        allcalories += 70
    if data['lunches'] == 'Mac and Cheese':
        allcalories += 187
    if data['lunches'] == 'Beef burger':
        allcalories += 120
    if data['lunches'] == 'Grilled Cheese':
        allcalories += 387
    


    return str(allcalories)