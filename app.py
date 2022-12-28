from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
db = SQLAlchemy()


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, primary_key=True)
    isActive = 0
    text = db.Column(db.Text, nullable=False)
    amount = db.Column(db.Integer, primary_key=True)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/catalog')
def catalog():
    return render_template('catalog.html')


if __name__ == '__main__':
    app.run(debug=True)