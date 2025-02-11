from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
db = SQLAlchemy(app)

class Item(db.Model):
    name = db.Column(db.String(length=30))
    price = db.Column(db.Float())


@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode':'897527993625', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode':'123456789790', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode':'987654321098', 'price': 150},
    ]
    return render_template('market.html', items=items)