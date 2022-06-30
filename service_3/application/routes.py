from application import app
import random

@app.route('/get_lunch', methods=['GET'])
def get_lunch():
    lunches = ['Veg Pizza', 'Chicken and chips', 'Chicken fried rice', 'Burger and Chips', 'Pa', 
    'Lentil soup', 'Mac and Cheese', 'Beef burger', 'Grilled Cheese', 'Ramen noodles' ]
    lunch = random.choice(lunches)
    return lunch