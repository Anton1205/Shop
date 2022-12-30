from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route('/')
@app.route('/home')
def home():
    items = Item.query.order_by(Item.price).all()
    return render_template('home.html', data=items)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/catalog')
def catalog():
    return render_template('catalog.html')


@app.route('/create', methods=['POST','GET'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        price = request.form['price']
        text = request.form['text']
        amount = request.form['amount']

        item = Item(title=title, price=price, text=text, amount=amount)

        try:
            db.session.add(item)
            db.session.commit()
            return redirect('/')
        except:
            return 'Произошла ошибка'

    else:
        return render_template('create.html')


@app.route('/create_app')
def create_app():
    #app = Flask(__name__)

    with app.app_context():
        db.init_app()

    return app


if __name__ == '__main__':
    app.run(debug=True)