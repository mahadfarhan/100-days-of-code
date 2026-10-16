# Day 61 — Flask-WTF Forms, Validation & Bootstrap

Day 61 of **100 Days of Code: The Complete Python Pro Bootcamp** focuses on building and validating web forms with Flask-WTF and WTForms, styling them using Bootstrap-Flask, and organizing pages through Jinja template inheritance.

The project is a small **Secrets** website with a login form. Submitting the form validates the supplied fields, checks the entered credentials against demo values, and renders either a success or access-denied page.

## Features

- Creates a Flask application with home and login routes
- Uses `FlaskForm` to define form fields in Python
- Includes email, password, and submit fields
- Applies WTForms validators to submitted data
- Handles both `GET` and `POST` requests on the login route
- Uses `validate_on_submit()` to process valid form submissions
- Conditionally renders success and denied pages based on demo credentials
- Integrates Bootstrap-Flask to render and style the form
- Uses a shared `base.html` template with Jinja inheritance and blocks
- Loads Bootstrap CSS and JavaScript from the base template
- Applies custom CSS to the shared page layout

## Technologies Used

- Python
- Flask
- Flask-WTF
- WTForms
- Bootstrap-Flask (`Bootstrap4`)
- Jinja2
- HTML and CSS
- `os` (random secret-key generation)

## Project — Secrets Login

### Flask Application (`main.py`)

The application is initialized with Bootstrap-Flask and a secret key:

```python
SECRET_KEY = os.urandom(32)

app = Flask(__name__)
bootstrap = Bootstrap4(app)
app.config["SECRET_KEY"] = SECRET_KEY
```

Flask-WTF uses the secret key for security features such as CSRF protection. In this exercise, the key is generated each time the application starts; restarting the app therefore changes it.

### Creating a Form with Flask-WTF

The login form is defined as a Python class:

```python
class MyForm(FlaskForm):
    email = StringField(label="Email", validators=[Email()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="Log In")
```

The `Email()` validator checks whether the email field contains a valid email format, while `DataRequired()` requires a non-empty password. `PasswordField` renders the password input as a masked form field.

### Processing GET and POST Requests

The `/login` route shows the form when visited and processes submissions when a valid form is posted:

```python
@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=form)
```

`validate_on_submit()` checks whether the request is a form submission and whether validation passes. Only then does the route compare the submitted values with the exercise's fixed credentials.

| Route | Purpose |
| --- | --- |
| `/` | Displays the homepage and a link to the login page |
| `/login` (`GET`) | Displays the login form |
| `/login` (`POST`) | Validates submitted data and displays success or denial |

Invalid form submissions return the login template with validation feedback instead of reaching the credential check.

### Template Inheritance (`templates/base.html`)

All pages extend a shared base template rather than repeating the same HTML structure:

```jinja2
{% extends "base.html" %}

{% block title %}Login{% endblock %}

{% block content %}
    <!-- Page-specific content -->
{% endblock %}
```

The base template defines `title`, `styling`, `content`, and `scripts` blocks. It loads Bootstrap assets and adds a purple page background:

```html
{% block styling %}
    {{ bootstrap.load_css() }}
    <style>
        body {background: purple;}
    </style>
{% endblock %}
```

This keeps shared page structure and styling in one place while allowing individual templates to supply their own content.

### Rendering the Login Form (`templates/login.html`)

Instead of manually writing the HTML for every input, the template imports Bootstrap-Flask's form-rendering helper:

```jinja2
{% from 'bootstrap4/form.html' import render_form %}

{% block content %}
<div class="container">
    <h1>Login</h1>
    {{ render_form(form, method="POST") }}
</div>
{% endblock %}
```

The form object is passed from Flask to Jinja, and the macro renders the form with Bootstrap-compatible markup.

### Success and Denied Pages

When submitted credentials match the exercise's values, `success.html` displays a **Top Secret** heading and a GIF. Otherwise, `denied.html` displays **Access Denied** and a different GIF. Both pages inherit from `base.html`.

## Application Flow

```text
Start Flask application
        ↓
Visit homepage (/)
        ↓
Click Login → GET /login
        ↓
Render Flask-WTF form
        ↓
Submit email and password → POST /login
        ↓
validate_on_submit()
        ↓
    Valid submission?
      ├── No → Render login form again
      └── Yes → Compare demo credentials
                    ├── Match → Success page
                    └── No match → Access Denied page
```

## Project Structure

```text
Day 61/
├── templates/
│   ├── base.html
│   ├── denied.html
│   ├── index.html
│   ├── login.html
│   └── success.html
├── main.py
└── requirements.txt
```

### File Overview

- **`main.py`** — Initializes Flask and Bootstrap, defines the WTForms form, registers routes, and handles submitted credentials.
- **`templates/base.html`** — Shared HTML layout, Bootstrap assets, CSS, and Jinja blocks.
- **`templates/index.html`** — Homepage with a link to the login form.
- **`templates/login.html`** — Bootstrap-rendered login form.
- **`templates/success.html`** — Successful demo login page.
- **`templates/denied.html`** — Access-denied page for nonmatching credentials.
- **`requirements.txt`** — Project dependency versions.

## Running the Project

Install the dependencies from the project folder:

```bash
pip install -r requirements.txt
```

Then start the Flask application:

```bash
python main.py
```

Open `http://127.0.0.1:5000/` in your browser and follow the **Login** link.

The exercise uses the following fixed demonstration credentials:

```text
Email: admin@email.com
Password: 12345678
```

> **Note:** This is a form-validation and template-inheritance exercise, not a complete authentication system. The credentials are hardcoded; the project does not use a user database, password hashing, login sessions, or account management. Do not reuse this approach to secure a real application.

## What I Learned

Day 61 introduces a more structured way of building web forms in Flask.

Key concepts included:

- Defining forms as Python classes that inherit from `FlaskForm`
- Creating text, password, and submit fields with WTForms
- Adding field-level validators
- Distinguishing between rendering a form and processing a submission
- Accessing validated form values through `.data`
- Handling `GET` and `POST` requests in one Flask route
- Using `validate_on_submit()` with Flask-WTF
- Understanding the role of a Flask secret key in CSRF protection
- Integrating Bootstrap-Flask with Jinja templates
- Importing and using the `render_form` macro
- Reusing layout, styles, and scripts with Jinja `{% extends %}` and `{% block %}`
- Rendering different pages based on conditional Python logic

## Development Notes

Day 61 builds directly on the Flask routing, dynamic templates, and HTML form handling from previous days.

The progression is:

**Flask routes → form classes → field validation → POST handling → conditional responses → template inheritance → Bootstrap styling**

Compared with manually retrieving values through `request.form`, Flask-WTF provides a form object that defines fields and validation rules together. Jinja inheritance also reduces repeated markup across multiple pages.

## Course Attribution

The project concepts and exercises originate from **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu. Any course-provided starter files, assets, and instructional patterns remain attributed to the course; this README does not claim them as original work.

## Disclosure

This README was written with AI assistance. **Any code authored by me in this repository was written independently by me.**

Course-provided instructional material, starter code, project structures, assets, and example implementations are not claimed as my original work.
