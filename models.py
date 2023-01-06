from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    isActive = db.Column(db.Boolean, default=True)
    text = db.Column(db.Text, nullable=False)
    amount = db.Column(db.Integer, nullable=False)


def __repr__(self):
    return '<Item %r' % self.id