# Day 56 — Rendering HTML Files with Flask

Day 56 of **100 Days of Code: The Complete Python Pro Bootcamp** builds on the Flask routing concepts introduced in Days 54 and 55 by serving an HTML template rather than returning HTML directly from a Python function.

The project is a **personal name card website** based on the **Identity** template by HTML5 UP. It displays a profile photo, name, professional title, and social-media icons. The Flask server renders the HTML template, while the styling, scripts, and profile image are referenced from the `static` directory. This introduces a cleaner way to structure web applications by separating route handling from page markup and supporting files.

## Features

- Creates a Flask web application
- Defines a home route using `@app.route()`
- Uses `render_template()` to return an HTML page
- Stores the page template in Flask's `templates` directory
- Organizes supporting assets and images under a `static` directory
- Displays a personal profile image, name, and professional title
- Includes social-media icon links in the page footer (currently placeholder `#` URLs)
- Uses the HTML5 UP Identity design template and its stylesheets
- Loads CSS, JavaScript, and image resources from Flask static paths
- Separates Python application logic from HTML page content
- Runs Flask's development server with debug mode enabled

## Technologies Used

- Python
- Flask
- HTML
- Flask's Jinja template rendering system
- HTML5
- CSS
- JavaScript
- HTML5 UP Identity template
- Static files and assets

## Project Overview

The application uses a simple Flask route to render `index.html` when a visitor opens the home page.

Instead of embedding HTML directly inside Python return statements, the project keeps the page in a separate template file. This makes the Python code responsible for handling the request and the HTML file responsible for defining the page.

## Flask Application (`name card/server.py`)

The server imports Flask and its `render_template()` function:

```python
from flask import Flask, render_template
```

A Flask application is then created:

```python
app = Flask(__name__)
```

### Home Route

The home route responds to requests for `/`:

```python
@app.route("/")
def home():
    return render_template("index.html")
```

When someone visits the application's root URL, Flask calls `home()` and renders `index.html` from the `templates` directory.

The key difference from Day 55 is that the view function no longer needs to contain the page's HTML markup as a long string.

### Running the Development Server

```python
if __name__ == "__main__":
    app.run(debug=True)
```

The `if __name__ == "__main__":` condition starts the development server when `server.py` is run directly.

Using `debug=True` enables Flask's development debugging features and automatic reload behavior when application code changes. Debug mode is intended for local development, not production deployment.

## HTML Template (`name card/templates/index.html`)

Flask looks for templates in a directory named `templates` by default. When the home route calls `render_template("index.html")`, Flask loads the HTML file and returns the page to the browser.

The page is based on **Identity by HTML5 UP**, with a main profile section containing an avatar, a name, and a role:

```html
<header>
    <span class="avatar"><img src="/static/images/avatar.jpeg" alt="" /></span>
    <h1>Mahad Bin Farhan</h1>
    <p>Junior Machine Learning Engineer & Data Scientist</p>
</header>
```

The page also contains a row of Twitter, Instagram, and Facebook icons. Their links currently use `href="#"`, so they are placeholders rather than functional profile links.

A larger form section is present in the HTML but commented out, so it is not displayed in the browser. The page also retains the HTML5 UP design credit in the footer.

The uploaded template contains regular HTML and asset references; it does not yet use Jinja variables, conditionals, or loops.

## Static Files

Flask uses `static/` to serve resources such as CSS, JavaScript, and images. The page references the profile photo at:

```html
<img src="/static/images/avatar.jpeg" alt="" />
```

It also links the main stylesheet from the template's assets folder:

```html
<link rel="stylesheet" href="/static/assets/css/main.css" />
```

Additional stylesheets support older browsers and no-JavaScript environments. An inline script removes the `is-loading` class from the page after it loads, supporting the template's loading transition.

The screenshot shows `static/assets/` and `static/images/`, but their individual contents were not uploaded for review. The HTML references files in those directories; their presence and rendering were not independently tested.

## Application Flow

```text
Start Flask application
         ↓
Visit the home page (/)
         ↓
Flask matches @app.route("/")
         ↓
Call home()
         ↓
render_template("index.html")
         ↓
Find index.html in templates/
         ↓
Render HTML template
         ↓
Return HTML response
         ↓
Browser displays the page
```

## Project Structure

```text
Day 56/
└── name card/
    ├── static/
    │   ├── assets/
    │   └── images/
    ├── templates/
    │   └── index.html
    └── server.py
```

### `server.py`

Creates the Flask application, registers the home route, renders the HTML template, and starts the local development server.

### `templates/index.html`

Contains the customized HTML5 UP Identity name card, including the profile header, social icon links, footer credit, linked stylesheets, and a short page-loading script.

### `static/assets/` and `static/images/`

Directories for the HTML5 UP design assets and profile image. The HTML references CSS and JavaScript under `assets/` and `avatar.jpeg` under `images/`; the underlying asset files were not included in the supplied materials.

## Running the Project

Install Flask if it is not already installed:

```bash
pip install flask
```

Navigate to the `name card` directory and start the application:

```bash
python server.py
```

Open the local URL printed by Flask, normally:

```text
http://127.0.0.1:5000/
```

Flask will render the `index.html` template when the root route is requested.

## What I Learned

Day 56 introduces template rendering and a more organized Flask application structure.

Key concepts included:

- Flask view functions can render separate HTML files
- `render_template()` loads a template from the `templates` directory
- Flask uses Jinja as its template-rendering engine
- HTML templates can be maintained separately from Python route logic
- The `static` directory provides a conventional location for assets and images
- HTML templates can reference CSS, JavaScript, and image files served through Flask
- A prebuilt HTML/CSS design can be customized into a personal name card
- HTML comments can retain sections of markup without displaying them
- Routes connect incoming requests to the HTML pages returned to the browser
- `debug=True` provides development-time debugging and reloading tools
- Separating the server, templates, and static resources makes a web project easier to organize

## Development Notes

Day 56 builds on the earlier Flask exercises by replacing inline HTML responses with a dedicated template file.

The progression is:

**Flask routes → HTML responses → external HTML templates → static assets → customized personal name card**

Day 55 used Python functions to return HTML strings. Day 56 instead uses Flask to load an HTML document from disk, keeping the page content separate from the request-handling logic.

The basic request-response workflow becomes:

**Browser request → Flask route → `render_template()` → HTML response → rendered webpage**

This provides a foundation for future Flask applications with multiple templates, shared assets, and more complex page content.

## Course Attribution

The project concepts and exercises originate from **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

## Disclosure

This README was written with AI assistance. **Any code authored by me in this repository was written independently by me.**

Course-provided instructional material, starter code, project structures, assets, and example implementations are not claimed as my original work.
