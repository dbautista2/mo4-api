from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(80), unique=True, nullable=False)
    publisher = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f'{self.name} - {self.author} - {self.id} - {self.publisher}'

    def create_app(self):
        app = Flask(__name__)

        return app


@app.route('/')
def index():
    return 'Hello'


@app.route('/books')
def get_books():

    return {'books': 'book data'}
