from flask import Flask, render_template, abort
import requests

app = Flask(__name__)


@app.route("/")
def index():
    response = requests.get("https://api.npoint.io/674f5423f73deab1e9a7")
    response.raise_for_status()

    all_posts = response.json()

    return render_template("index.html", posts=all_posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:blog_id>")
def blog_post(blog_id):
    response = requests.get("https://api.npoint.io/674f5423f73deab1e9a7")
    response.raise_for_status()

    all_posts = response.json()

    for post in all_posts:
        if post["id"] == blog_id:
            return render_template("post.html", post=post)

    abort(404)


if __name__ == "__main__":
    app.run(debug=True)
