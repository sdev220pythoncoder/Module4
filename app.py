from flask import Flask, request
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    book_name = db.Column(db.String(80),unique = True, nullable = False)
    author = db.Column(db.String(80), nullable =False)
    publisher = db.Column(db.String(80), nullable = False)

    def __repr__(self):
        return f"{self.book_name} - {self.author} - {self.publisher}"

@app.route("/")
def index():
    return "Hello, Flask!"

@app.route("/books")
def get_books() :
    books = Book.query.all()
    output = []
    for book in books :
        book_data = {'id':book.id, 
                     'book_name':book.book_name,
                     'author':book.author,
                     'publisher':book.publisher
                       }
        output.append(book_data)
    return {"Books":output}

@app.route('/books/<id>')
def get_book(id):   
    book = Book.query.get_or_404(id)
    return {"book_name":book.book_name,"author":book.author,"publisher":book.publisher}
