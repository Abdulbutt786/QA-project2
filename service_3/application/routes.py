from application import app
import random

@app.route('/get_lunch', methods=['GET'])
def get_lunch():
    lunches = ['Pizza', 'Chicken and chips', '', '', '', 
    '', '', '', '', '' ]
    lunch = random.choice(lunches)
    return lunch