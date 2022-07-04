from application import db

class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    breakfast = db.Column(db.String(50), nullable = False)
    lunch = db.Column(db.String(50), nullable = False)
    price = db.Column(db.Integer(), nullable=False)