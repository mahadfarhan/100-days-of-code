# Day 64 — Top 10 Movies Website with Flask, SQLAlchemy & TMDB API

Day 64 of **100 Days of Code: The Complete Python Pro Bootcamp** builds on the database and Flask concepts from Day 63 by creating a **Top 10 Movies** website for maintaining a personal collection of favourite films.

The application combines Flask routes, Flask-WTF forms, a SQLite database managed through SQLAlchemy, and **The Movie Database (TMDB) API**. Movies can be searched by title, selected from TMDB results, added to the local database, rated, reviewed, ranked, and deleted. The project also includes an Alembic configuration for database migrations.

## Features

- Displays saved movies in descending order of personal rating
- Assigns ranking numbers based on the current rating order
- Shows movie posters, titles, release years, ratings, reviews, and descriptions
- Uses interactive, CSS-styled movie cards with front and back views
- Searches TMDB for movies by title
- Displays matching results for the user to select a specific film
- Retrieves the selected movie's details and poster from TMDB
- Saves chosen movies to a persistent SQLite database
- Provides Flask-WTF forms for adding movie titles and editing ratings and reviews
- Updates and deletes saved movie records by their database IDs
- Redirects after database changes to show the updated collection
- Includes Alembic configuration and migration files for schema changes

## Technologies Used

- Python
- Flask
- Flask-SQLAlchemy
- SQLAlchemy ORM
- SQLite
- Flask-WTF and WTForms
- Bootstrap-Flask (`Bootstrap5`)
- Jinja2
- HTML and CSS
- `requests`
- TMDB API
- `python-dotenv`
- Alembic

## Project Overview

### Flask Application and Database Configuration (`main.py`)

The project initializes Flask, Bootstrap-Flask, and SQLAlchemy. Movie data is stored in a SQLite database named `project.db` under Flask's `instance` directory.

```python
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
Bootstrap5(app)

class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
db.init_app(app)
```

The application also configures a Flask secret key for Flask-WTF. In the supplied implementation, this key is hardcoded in `main.py`; it should be moved to an environment variable before deployment.

### Movie Database Model

The `Movie` model defines the information stored for each film:

```python
class Movie(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True, nullable=False)
    year: Mapped[int] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    rating: Mapped[float] = mapped_column(nullable=True)
    ranking: Mapped[int] = mapped_column(nullable=True)
    review: Mapped[str] = mapped_column(nullable=True)
    img_url: Mapped[str] = mapped_column(nullable=False)
```

Each record contains a unique ID, title, release year, description, and poster URL. Rating, ranking, and review fields can be empty when a movie is first added.

When the application is run directly, `db.create_all()` creates any missing database tables. Existing records are retained between restarts.

### Viewing and Ranking Movies (`/`)

The homepage retrieves stored movies in descending order of rating:

```python
@app.route("/")
def home():
    all_movies = (
        db.session.execute(db.select(Movie).order_by(Movie.rating.desc()))
        .scalars()
        .all()
    )
    for i in range(len(all_movies)):
        all_movies[i].ranking = i + 1
    db.session.commit()
    return render_template("index.html", movies=all_movies)
```

The route recalculates each movie's ranking from its position in the ordered results and commits those rankings to the database. `index.html` displays each film as a poster card, with the movie's details, personal score, review, and Update/Delete links on the reverse side.

**Note:** Despite the project's *Top 10 Movies* title, the current query does not apply a ten-movie limit; it displays every movie stored in the database.

### Searching for Movies (`/add`)

A Flask-WTF form collects a movie title:

```python
class AddMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")
```

When the form is submitted, the application sends a request to TMDB's movie search endpoint:

```python
url = "https://api.themoviedb.org/3/search/movie"
headers = {"accept": "application/json", "Authorization": BEARER_TOKEN}
parameters = {"query": form.title.data}
response = requests.get(url, headers=headers, params=parameters)
```

The application processes the first page of results and fetches a second page when available. Each result is represented by its title, release date, and TMDB movie ID. The matches are passed to `select.html`, allowing the visitor to choose the intended movie rather than automatically selecting the first match.

### Adding a Selected Movie (`/add-movie/<int:id>`)

After a result is selected, the application requests that movie's details using its TMDB ID:

```python
url = f"https://api.themoviedb.org/3/movie/{id}"
response = requests.get(url, headers=headers)
response.raise_for_status()

data = response.json()
new_movie = Movie(
    title=data["title"],
    year=int(data["release_date"][0:4]),
    description=data["overview"],
    img_url=f"https://image.tmdb.org/t/p/w500{data['poster_path']}",
)
db.session.add(new_movie)
db.session.commit()
```

TMDB supplies the title, year, description, and poster path. The application saves these details locally, then redirects to the edit page so the user can enter a personal rating and review.

The same title cannot be inserted twice because the database model applies a unique constraint to `title`.

### Editing Ratings and Reviews (`/edit/<int:id>`)

A second Flask-WTF form collects a numerical rating and written review:

```python
class MyForm(FlaskForm):
    rating = FloatField("Your Rating out of 10 e.g 7.5", validators=[InputRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField("Done")
```

The edit route retrieves the selected movie using `db.get_or_404()`, then updates its values after successful form validation:

```python
movie_to_edit = db.get_or_404(Movie, id)

if form.validate_on_submit():
    movie_to_edit.rating = form.rating.data
    movie_to_edit.review = form.review.data
    db.session.commit()
    return redirect(url_for("home"))
```

Using `db.get_or_404()` returns a 404 response if the requested movie does not exist. A successful update redirects to the homepage, where the rankings are recalculated based on the new ratings.

### Deleting Movies (`/delete/<int:id>`)

The delete route looks up the movie by its database ID, removes it from the database session, commits the change, and returns to the homepage:

```python
@app.route("/delete/<int:id>")
def delete(id):
    movie_to_delete = db.get_or_404(Movie, id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for("home"))
```

This completes the application's basic CRUD functionality: creating, reading, updating, and deleting movie records.

### HTML Templates and Movie Card Styling

The website uses Jinja templates and a shared `base.html` layout:

- `base.html` — Loads Bootstrap, fonts, Font Awesome, and custom styles.
- `index.html` — Displays the ranked movie collection, movie cards, and Update/Delete actions.
- `add.html` — Renders the movie-title search form.
- `select.html` — Lists TMDB search matches as selectable links.
- `edit.html` — Renders the rating and review form for a selected movie.

The `static/css/styles.css` file styles the movie cards, responsive layout, buttons, and hover-based 3D card-flip transitions. TMDB poster images appear on the front of each card, while the reverse contains the movie's information.

### Database Migrations with Alembic

The project includes Alembic migration configuration alongside the SQLite database. The `alembic.ini` file identifies the migration script directory and database URL:

```ini
script_location = %(here)s/alembic
sqlalchemy.url = sqlite:///./instance/project.db
```

The `alembic/env.py` file imports the declarative base from `main.py` and supplies its metadata for migration operations:

```python
from main import Base

target_metadata = Base.metadata
```

Its online migration configuration also enables `render_as_batch=True`, a useful option when applying certain table changes to SQLite. The project directory contains a versioned migration script, and the supplied database includes an `alembic_version` table.

Alembic provides a way to manage schema changes beyond `db.create_all()`, which creates missing tables but does not migrate existing table structures.

## Application Flow

```text
Start Flask application
         ↓
Initialize SQLAlchemy / create missing tables
         ↓
Open homepage (/)
         ↓
Load saved movies → Sort by rating → Assign rankings
         ↓
Render movie cards in index.html
         ↓
    Choose an action
         │
         ├── Add Movie (/add)
         │      ↓
         │   Enter title → Submit form
         │      ↓
         │   Search TMDB → Display matching movies
         │      ↓
         │   Select movie (/add-movie/<id>)
         │      ↓
         │   Fetch TMDB details → Insert record → Commit
         │      ↓
         │   Redirect to Edit → Add rating and review
         │      ↓
         │   Commit → Redirect home
         │
         ├── Update (/edit/<id>)
         │      ↓
         │   Find movie → Submit new rating/review
         │      ↓
         │   Commit → Redirect home
         │
         └── Delete (/delete/<id>)
                ↓
             Find movie → Delete → Commit → Redirect home
```

## Project Structure

```text
Day 64/
├── alembic/
│   ├── versions/
│   │   └── 0262311410abe_changed_3_values_fr...py
│   ├── env.py
│   ├── README
│   └── script.py.mako
├── instance/
│   └── project.db
├── static/
│   └── css/
│       └── styles.css
├── templates/
│   ├── add.html
│   ├── base.html
│   ├── edit.html
│   ├── index.html
│   └── select.html
├── .env                  # Local API credentials; do not commit
├── alembic.ini
├── main.py
└── requirements.txt
```

The diagram omits generated `__pycache__` directories. The migration file name is shortened to reflect the visible project tree.

### Main Project Files

- **`main.py`** — Defines Flask routes, forms, the `Movie` model, TMDB API requests, ranking logic, and database operations.
- **`templates/index.html`** — Renders the ranked movie cards and actions.
- **`templates/add.html`** — Provides the movie search form.
- **`templates/select.html`** — Presents TMDB search results for selection.
- **`templates/edit.html`** — Provides the personal rating and review form.
- **`templates/base.html`** — Shared HTML structure and stylesheet links.
- **`static/css/styles.css`** — Custom card layouts, animations, and responsive styling.
- **`instance/project.db`** — Persistent SQLite database containing movie records.
- **`alembic.ini` and `alembic/`** — Database migration configuration and scripts.

## Running the Project

Install dependencies from the project directory:

```bash
pip install -r requirements.txt
pip install python-dotenv alembic
```

The second command installs two packages used by the project but not listed in the supplied `requirements.txt`.

Obtain TMDB API credentials and create a `.env` file in the project directory:

```dotenv
TMDB_API=your_tmdb_api_key
BEARER_TOKEN=Bearer your_tmdb_read_access_token
```

The current application uses `BEARER_TOKEN` for its TMDB requests; `TMDB_API` is loaded but not otherwise used. The `Authorization` header expects the bearer-token prefix as part of the configured value.

Start the application:

```bash
python main.py
```

Open the local Flask server, normally `http://127.0.0.1:5000/`.

The database tables are created if they do not already exist, and movies remain saved after restarting the app. An internet connection and valid TMDB credentials are required to search for and add new movies.

To inspect the existing Alembic migration state from the project directory:

```bash
alembic current
alembic history
```

Apply outstanding migration scripts, when appropriate for the database:

```bash
alembic upgrade head
```

Do not run migrations against important data without first reviewing the scripts and backing up the database.

## What I Learned

Day 64 combines Flask form handling, persistent database records, and an external API to build a more complete web application.

Key concepts included:

- Defining database models using SQLAlchemy's typed ORM syntax
- Storing both required and optional movie information in SQLite
- Querying records and ordering them by a numerical field
- Recalculating rankings after ratings change
- Using `db.get_or_404()` for missing database records
- Creating and validating forms with Flask-WTF
- Handling GET and POST requests in the same route
- Searching a third-party API using query parameters
- Passing API authorization through request headers
- Processing JSON responses and paginated search results
- Fetching detailed data for a selected API result
- Constructing poster-image URLs from API data
- Saving external API data in a local relational database
- Redirecting users between search, selection, edit, and listing pages
- Performing CRUD operations with SQLAlchemy sessions
- Using Jinja templates to render database-backed content
- Applying CSS-based flip-card effects to a responsive interface
- Introducing Alembic migration configuration for schema changes

## Development Notes

Day 64 builds directly on the Day 63 book library. Instead of manually entering all of a record's details, the application retrieves movie metadata from TMDB and saves it locally. Users then add their own ratings and reviews, which determine how the movies are ranked.

The overall progression is:

**Flask forms → TMDB movie search → movie selection → API detail retrieval → SQLite persistence → rating and review updates → dynamic ranking**

This is a course project rather than a production-ready movie collection system. Important limitations of the current implementation include:

- The homepage displays all movies rather than enforcing a top-ten limit.
- Rankings are written to the database whenever the homepage is visited.
- The rating field accepts floating-point input but has no explicit 0–10 range validator.
- Movie search and detail requests have limited error handling, and results are assumed to contain fields such as release dates and poster paths.
- Duplicate movie titles can cause a database uniqueness error.
- Deletion uses a GET route rather than a confirmed, CSRF-protected POST action.
- The Flask secret key is hardcoded, and the application runs with `debug=True`.
- `python-dotenv` and Alembic are not currently included in `requirements.txt`.

These are opportunities for further improvement rather than features implemented in the supplied project.

## Course Attribution

The project concepts, exercises, and instructional materials originate from **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

Movie metadata and posters are retrieved from **The Movie Database (TMDB)**. The supplied front-end templates and styling are not claimed as original design work.

## Disclosure

This README was written with AI assistance. **Any code authored by me in this repository was written independently by me.**

Course-provided instructional material, starter code, project structures, assets, and example implementations are not claimed as my original work.
