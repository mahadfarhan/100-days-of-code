from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from pathlib import Path
import sqlite3

# db = sqlite3.connect("./sqlite exercise/books-collection.db")
# cursor = db.cursor()
# cursor.execute(
#     "CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)"
# )
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

app = Flask(__name__, instance_path=str(Path(__file__).resolve().parent / "instance"))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

db.init_app(app)


class Books(db.Model):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(nullable=False)


book_1 = Books(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)

with app.app_context():
    db.create_all()
    db.session.add(book_1)
    db.session.commit()
