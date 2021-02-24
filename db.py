from flask import current_app
from flask_sqlalchemy import SQLAlchemy
from config import DB_URI

current_app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
current_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(current_app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False, unique=True)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    author = db.Column(db.String(30))
    publisher = db.Column(db.String(30))
    publication_date = db.Column(db.Date)
    pages = db.Column(db.Integer)
    isbn = db.Column(db.Integer)
    description = db.Column(db.Text)
    link = db.Column(db.Text)
    image = db.Column(db.String(10))
    rating = db.Column(db.Integer)
    available = db.Column(db.Integer)


def init_db():
    # bind db and app
    db.init_app(current_app)
    db.drop_all()
    db.create_all()

    sample_book1 = Book(
        name='Harry Potter',
        author='Rolling',
        pages=250,
        rating=4,
        available=10
    )
    sample_book2 = Book(
        name='LOTR',
        author='Tolkin',
        pages=1000,
        rating=5,
        available=4
    )
    db.session.add(sample_book1)
    db.session.add(sample_book2)
    db.session.commit()
