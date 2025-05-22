import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, 'book_db.sqlite')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Books(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.String(50), nullable=False)
   author = db.Column(db.String(50), nullabl =False)
   price = db.Column(db.Float, nullable=False)

def __str__(self)
    return f"title: {self.title}, author: {self.author} price: {self.price}"
with app.app_context():
  book1 = Books.query.first()
  all_books = Books_query.all()
  rowling_books = Books.query.filter_by(author=rowling).all()
  for Book in all_books
      print(Book)
  print(book1)

title = "sdsd"
author = "scs"
price = 33
new_book = books(title=title,author=author,price=price)

db.session.add(books())
db.session.commit()
