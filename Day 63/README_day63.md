# Day 63 — SQLite, SQLAlchemy & Flask Book Library

Day 63 of **100 Days of Code: The Complete Python Pro Bootcamp** introduces persistent data storage using SQLite and SQLAlchemy, then applies those concepts to a Flask-based book library.

The work consists of a **SQLite/SQLAlchemy exercise** and a **book collection web app** where books can be added, displayed, rated, and deleted through Flask routes and HTML templates.

## Features

- Creates and connects to SQLite databases
- Defines a `Books` model using SQLAlchemy's modern typed ORM syntax
- Creates database tables from model definitions
- Inserts and commits database records
- Queries books and sorts them alphabetically by title
- Displays stored books in a Jinja-rendered HTML page
- Adds books from a form using a POST request
- Updates an existing book's rating using its database ID
- Deletes a book record by ID
- Uses redirects after form submissions
- Separates frontend templates from Flask routes and database logic

## Technologies Used

- Python
- Flask
- Flask-SQLAlchemy
- SQLAlchemy ORM
- SQLite
- `sqlite3` (introductory exercise)
- HTML
- Jinja2

## Exercises

### SQLite & SQLAlchemy (`sqlite exercise/main.py`)

The first exercise explores how a database stores book records. It includes commented examples using Python's built-in `sqlite3` library to create a table and insert a record using SQL statements.

The active implementation uses Flask-SQLAlchemy and a SQLite file named `new-books-collection.db` in the exercise's `instance` directory.

A declarative base is configured and a `Books` model defines the table structure:

```python
class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class Books(db.Model):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(nullable=False)
```

Each book has a unique ID, title, author, and rating. The exercise creates the table and inserts an example *Harry Potter* record:

```python
with app.app_context():
    db.create_all()
    db.session.add(book_1)
    db.session.commit()
```

**Note:** The exercise inserts a book with a fixed ID every time the script runs. Running it again against the same populated database may raise a uniqueness or primary-key constraint error.

### Book Library (`main.py`)

The main project builds on the database exercise to create a small Flask web application backed by `project.db`.

#### Database Configuration

```python
app = Flask(__name__)

class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)
```

The application uses the same `Books` ORM model to represent records in the library.

When the application is started directly, the database tables are created inside Flask's application context:

```python
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

#### Viewing Books (`/`)

The home route selects books from the database and orders them by title:

```python
@app.route("/")
def home():
    result = db.session.execute(db.select(Books).order_by(Books.title))
    all_books = result.scalars().all()
    return render_template("index.html", books=all_books)
```

`index.html` loops through the books and provides links to edit a rating or delete a record. It also displays an empty-library message when no books are passed to the template.

#### Adding a Book (`/add`)

The `/add` endpoint accepts both GET and POST requests. GET displays the form, while POST reads the submitted title, author, and rating:

```python
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        book = Books(
            title=request.form["name"],
            author=request.form["author"],
            rating=request.form["rating"],
        )
        db.session.add(book)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html")
```

The new book is committed to SQLite, and the user is redirected to the library page.

#### Editing a Rating (`/edit/<int:id>`)

The edit route uses the book's ID from the URL to retrieve the relevant database record:

```python
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    book = db.session.get(Books, id)
    if request.method == "POST":
        book.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", book=book)
```

The GET request displays the book's current rating; submitting a new rating updates the stored record.

#### Deleting a Book (`/delete/<int:id>`)

The delete route retrieves the selected book, removes it from the session, and commits the change:

```python
@app.route("/delete/<int:id>")
def delete(id):
    book = db.session.get(Books, id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("home"))
```

After committing the deletion, the route redirects to `home`, which queries the database again and displays the updated book collection. This avoids rendering the library template with an outdated or missing `books` variable.

## Application Flow

```text
Start Flask application
         ↓
Initialize SQLAlchemy and create missing tables
         ↓
Open library homepage (/)
         ↓
Query books → Render index.html
         ↓
   Choose an action
         │
         ├── Add book (/add)
         │      ↓
         │   Submit form → Insert record → Commit → Redirect home
         │
         ├── Edit rating (/edit/<id>)
         │      ↓
         │   Find book → Update rating → Commit → Redirect home
         │
         └── Delete book (/delete/<id>)
                ↓
             Find book → Delete record → Commit → Redirect home
```

## Project Structure

```text
Day 63/
├── instance/
│   └── project.db
├── sqlite exercise/
│   ├── instance/
│   │   └── new-books-collection.db
│   └── main.py
├── templates/
│   ├── add.html
│   ├── edit.html
│   └── index.html
├── main.py
└── requirements.txt
```

### Main Project Files

- **`main.py`** — Defines the Flask application, database model, and routes for listing, adding, editing, and deleting books.
- **`templates/index.html`** — Displays the library, book ratings, and action links.
- **`templates/add.html`** — Contains the form for adding books.
- **`templates/edit.html`** — Displays a book's current rating and a form to change it.
- **`instance/project.db`** — SQLite database file used by the Flask library.
- **`sqlite exercise/main.py`** — Demonstrates SQLite and SQLAlchemy fundamentals.

## Running the Project

Install dependencies from the project folder:

```bash
pip install -r requirements.txt
```

Run the main application:

```bash
python main.py
```

Open the address printed by Flask, normally `http://127.0.0.1:5000/`.

The book library database is created if it does not already exist. Its contents persist between application restarts.

To explore the separate database exercise, run its `main.py` from the `sqlite exercise` folder. Be aware that rerunning the exercise against the same database may attempt to insert the same sample book again.

## What I Learned

Day 63 introduces a major change from storing application data in local variables or flat files to working with a relational database.

Key concepts included:

- SQLite stores structured records persistently
- SQLAlchemy maps Python model classes to database tables
- `Mapped` and `mapped_column()` describe model fields
- Primary keys uniquely identify records
- Database constraints can enforce required and unique values
- `db.create_all()` creates missing tables
- `db.session.add()` stages an inserted record
- `db.session.commit()` saves changes
- `db.select()` and `order_by()` retrieve and sort records
- `db.session.get()` looks up a record by primary key
- Model attributes can be updated before committing
- `db.session.delete()` marks a record for deletion
- Dynamic Flask routes can identify individual database records
- HTML forms and Jinja templates connect the database to the user interface

## Development Notes

This project combines Flask routing, HTML forms, Jinja rendering, and SQLAlchemy to implement basic **CRUD** operations:

**Create → Read → Update → Delete**

The overall progression is:

**SQLite fundamentals → ORM models → database queries → Flask forms → persistent web application**

This is a learning project rather than a production-ready library system. Additional improvements could include missing-record handling, validated numeric ratings, and POST-based deletion.

## Course Attribution

The project concepts, exercises, and instructional materials originate from **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

## Disclosure

This README was written with AI assistance. **Any code authored by me in this repository was written independently by me.**

Course-provided instructional material, starter code, project structures, assets, and example implementations are not claimed as my original work.
