from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def home():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    response.raise_for_status()

    all_posts = response.json()

    return render_template("index.html", posts=all_posts)


@app.route("/post/<int:blog_id>")
def blog_post(blog_id):
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    response.raise_for_status()

    all_posts = response.json()

    for post in all_posts:
        if post["id"] == blog_id:
            return render_template("post.html", post=post, id=int(blog_id))


if __name__ == "__main__":
    app.run(debug=True)
