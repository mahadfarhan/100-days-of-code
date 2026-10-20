from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, InputRequired
import requests
import os
from dotenv import load_dotenv

load_dotenv()

TMDB_API = os.getenv("TMDB_API")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
Bootstrap5(app)


# CREATE DB
class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
db.init_app(app)


class MyForm(FlaskForm):
    rating = FloatField("Your Rating out of 10 e.g 7.5", validators=[InputRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField("Done")


class AddMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True, nullable=False)
    year: Mapped[int] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    rating: Mapped[float] = mapped_column(nullable=True)
    ranking: Mapped[int] = mapped_column(nullable=True)
    review: Mapped[str] = mapped_column(nullable=True)
    img_url: Mapped[str] = mapped_column(nullable=False)


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


@app.route("/edit/<int:id>", methods=["POST", "GET"])
def edit(id):

    form = MyForm()
    movie_to_edit = db.get_or_404(Movie, id)

    if form.validate_on_submit():
        movie_to_edit.rating = form.rating.data
        movie_to_edit.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form=form, movie=movie_to_edit)


@app.route("/delete/<int:id>")
def delete(id):
    movie_to_delete = db.get_or_404(Movie, id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=["POST", "GET"])
def add():
    list_of_movies = []
    url = "https://api.themoviedb.org/3/search/movie"
    headers = {"accept": "application/json", "Authorization": BEARER_TOKEN}
    form = AddMovieForm()

    if form.validate_on_submit():
        parameters = {"query": form.title.data}
        response = requests.get(url, headers=headers, params=parameters)
        total_pages = min(2, response.json()["total_pages"])

        for result in response.json()["results"]:
            list_of_movies.append(
                {
                    "title": f"{result['title']} - {result['release_date']}",
                    "id": result["id"],
                }
            )

        for page in range(2, total_pages + 1):
            parameters = {"query": form.title.data, "page": page}
            response = requests.get(url, headers=headers, params=parameters)
            for result in response.json()["results"]:
                list_of_movies.append(
                    {
                        "title": f"{result['title']} - {result['release_date']}",
                        "id": result["id"],
                    }
                )

        return render_template(
            "select.html",
            movies=list_of_movies,
        )

    return render_template("add.html", form=form)


@app.route("/add-movie/<int:id>")
def add_movie(id):
    url = f"https://api.themoviedb.org/3/movie/{id}"
    headers = {"accept": "application/json", "Authorization": BEARER_TOKEN}
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    data = response.json()
    new_movie = Movie(
        title=data["title"],
        year=int(data["release_date"][0:4]),
        description=data["overview"],
        img_url=f"https://image.tmdb.org/t/p/w500{data["poster_path"]}",
    )
    db.session.add(new_movie)
    db.session.commit()

    return redirect(url_for("edit", id=new_movie.id))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
