from application import app
import random

@app.route('/get_breakfast', methods=['GET'])
def breakfast():
    breakfasts = ['Bread and eggs', 'French Toast', 'Nuts and Seeds Granola','Norwegian Risgrøt Rice Porridge.',
        'Cheesy skillet hash brown & eggs','Pancakes', 'Waffles with stawberries']
    breakfast = random.choice(breakfasts)
    return breakfast