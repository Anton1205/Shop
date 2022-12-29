from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.sqlite'


db.init_app(app)


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


@app.route('/create')
def create():
    return render_template('create.html')


@app.route('/create_app')
def create_app():
    #app = Flask(__name__)

    with app.app_context():
        db.init_app()

    return app


if __name__ == '__main__':
    app.run(debug=True)