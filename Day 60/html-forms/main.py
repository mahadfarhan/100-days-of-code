from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    submitted = False
    return render_template("index.html", submitted=submitted)


@app.route("/login", methods=["POST"])
def receive_data():
    submitted = True
    username = request.form["username"]
    password = request.form["password"]
    print(request.form)
    return render_template(
        "index.html", username=username, password=password, submitted=submitted
    )


if __name__ == "__main__":
    app.run(debug=True)
