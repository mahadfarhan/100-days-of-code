from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv
import os
import smtplib

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)

load_dotenv()

my_email = os.getenv("MY_EMAIL")
password = os.getenv("EMAIL_PASSWORD")
send_to = os.getenv("SEND_TO")


@app.route("/")
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "GET":
        return render_template("contact.html", submitted=False)
    elif request.method == "POST":
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=send_to,
                msg=f"""Subject: New Message!\n\n
                
                Name: {request.form['name']}
                Email Address: {request.form['email']}
                Phone Number: {request.form['phone']}
                Message: {request.form['message']}
                """,
            )
        return render_template("contact.html", submitted=True)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
