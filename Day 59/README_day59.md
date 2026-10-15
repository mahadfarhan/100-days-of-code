# Day 59 — Upgraded Blog with Flask, Jinja & Bootstrap

Day 59 of **100 Days of Code: The Complete Python Pro Bootcamp** expands the Flask blog project into a multi-page website using a provided **Start Bootstrap Clean Blog** design. The project combines API-sourced blog content, dynamic routes, Jinja templating, and reusable page components.

Most of the front-end starter code and styling were provided as part of the exercise. **I wrote `main.py` independently**, created/separated the reusable `header.html` and `footer.html` templates, and integrated those components and the dynamic blog content into the site's pages.

## Features

- Runs a multi-page blog using Flask
- Retrieves blog post data from an external JSON API with `requests`
- Displays blog titles and subtitles dynamically on the home page
- Generates links to individual blog posts using their IDs
- Renders each post's title, subtitle, body, and header image
- Provides separate Home, About, and Contact routes
- Uses Jinja `{% for %}` loops to render a collection of posts
- Uses Jinja `{% include %}` to share the header and footer between pages
- Uses `url_for()` to generate links to routes and static assets
- Returns a 404 response when a requested blog post ID is not found
- Uses the supplied Bootstrap-based styling, images, and JavaScript assets

## Technologies Used

- Python
- Flask
- Jinja2
- `requests`
- HTML
- CSS
- Bootstrap / Start Bootstrap Clean Blog theme
- JavaScript (provided theme assets)
- JSON API

## Project Structure

```text
Day 59/
└── startbootstrap-clean-blog/   # Project folder (name may vary)
    ├── main.py
    ├── templates/
    │   ├── index.html
    │   ├── post.html
    │   ├── about.html
    │   ├── contact.html
    │   ├── header.html
    │   └── footer.html
    └── static/
        ├── assets/
        │   ├── img/
        │   └── favicon.ico
        ├── css/
        │   └── styles.css
        └── js/
            └── scripts.js
```

## Flask Backend (`main.py`)

I wrote the Flask application to connect the provided pages to live API data and handle navigation between blog posts.

### Home Page (`/`)

The home route requests the blog post collection, checks the HTTP response, converts the JSON into Python data, and supplies the posts to `index.html`:

```python
@app.route("/")
def index():
    response = requests.get("https://api.npoint.io/674f5423f73deab1e9a7")
    response.raise_for_status()

    all_posts = response.json()

    return render_template("index.html", posts=all_posts)
```

The template then loops through the returned posts and displays each title and subtitle:

```html
{% for post in posts: %}
<div class="post-preview">
    <a href="{{ url_for('blog_post', blog_id=post['id']) }}">
        <h2 class="post-title">{{ post['title'] }}</h2>
        <h3 class="post-subtitle">{{ post['subtitle'] }}</h3>
    </a>
</div>
{% endfor %}
```

Each link points to a route corresponding to that post's ID.

### Individual Blog Posts (`/post/<int:blog_id>`)

The post route captures an integer from the URL, fetches the post collection, and searches for the matching ID:

```python
@app.route("/post/<int:blog_id>")
def blog_post(blog_id):
    response = requests.get("https://api.npoint.io/674f5423f73deab1e9a7")
    response.raise_for_status()

    all_posts = response.json()

    for post in all_posts:
        if post["id"] == blog_id:
            return render_template("post.html", post=post)

    abort(404)
```

In `post.html`, Jinja inserts the selected post's content, including its image URL:

```html
<header class="masthead" style="background-image: url('{{ post.image_url }}')">
    <!-- Page heading -->
</header>

<h1>{{ post['title'] }}</h1>
<h2>{{ post['subtitle'] }}</h2>
<p>{{ post['body'] }}</p>
```

If no post has the requested ID, `abort(404)` tells Flask to return a Not Found response instead of silently failing.

### About and Contact Pages

Two additional routes render the corresponding templates:

```python
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")
```

These pages use the supplied page layouts and the shared header and footer. The Contact page currently contains the starter theme's form markup; **this project does not implement Flask-side form processing or email submission**.

## Reusable Header and Footer

Rather than repeating the same navigation and footer markup in each page, I separated these sections into `header.html` and `footer.html` and included them where needed:

```html
{% include 'header.html' %}

<!-- Page-specific content -->

{% include 'footer.html' %}
```

The header contains shared document-head resources and navigation links. The footer contains the theme's footer layout and script references.

The navigation uses Flask's `url_for()` helper instead of hardcoding most page URLs:

```html
<a href="{{ url_for('index') }}">Home</a>
<a href="{{ url_for('about') }}">About</a>
<a href="{{ url_for('contact') }}">Contact</a>
```

Static assets are also linked through Flask:

```html
<link href="{{ url_for('static', filename='css/styles.css') }}" rel="stylesheet" />
<script src="{{ url_for('static', filename='js/scripts.js') }}"></script>
```

This makes shared page elements easier to maintain and keeps asset paths aligned with Flask's directory structure.

## Application Flow

```text
Start Flask application
        ↓
Visit / (home page)
        ↓
Request blog JSON from API
        ↓
Parse returned posts
        ↓
Render index.html with Jinja
        ↓
Display each post title and subtitle
        ↓
Click a post link
        ↓
Visit /post/<blog_id>
        ↓
Fetch posts and find matching ID
        ↓
    ┌──────────────────────────┐
    │ Matching post found?     │
    └────────────┬─────────────┘
           Yes   │   No
            ↓    │    ↓
    Render post  │  Return 404
    with content │
```

The navigation also supports independent `/about` and `/contact` pages.

## Running the Project

Install the dependencies:

```bash
pip install flask requests
```

Run the Flask application from the project directory:

```bash
python main.py
```

Open the address printed by Flask, normally:

```text
http://127.0.0.1:5000/
```

The site requires an internet connection to retrieve blog data from the external API and to load externally hosted resources used by the template.

## What I Learned

Day 59 built on the Flask and Jinja concepts from earlier days and showed how they fit into a larger, multi-page website.

Key concepts included:

- Connecting Flask route functions to a complete front-end template
- Separating reusable HTML into partial templates
- Including shared layouts with Jinja's `{% include %}`
- Passing lists and dictionaries from Python into templates
- Iterating through API-sourced content with Jinja loops
- Using dynamic route parameters to identify individual posts
- Linking to Flask endpoints with `url_for()`
- Serving stylesheets, scripts, and images from the `static` directory
- Handling missing records with `abort(404)`
- Integrating an existing design without claiming the supplied design assets as original work

## Development Notes

The main progression for this project was:

**Provided Bootstrap layout → reusable Jinja components → Flask routes → API-powered post listings → individual post pages → missing-post handling**

The biggest step forward from the earlier blog exercise was integrating the backend logic with a more complete website structure. Shared header and footer templates avoid duplicating common markup, while Flask determines which page and post data to render.

The current project is a course exercise rather than a production-ready blogging platform. Blog content comes from an external API; there is no database, admin interface, or post editor. The contact form is starter UI and is not connected to a backend submission handler. Some template links, labels, and dates remain placeholders from the supplied design.

## Course Attribution

The project concepts and exercise originate from **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

The front-end design is based on the **Clean Blog** template by [Start Bootstrap](https://startbootstrap.com/theme/clean-blog). Much of the supplied HTML, CSS, JavaScript, and visual styling originates from the starter materials/template.

## Disclosure

This README was written with AI assistance. **I wrote `main.py` independently**, and my project work included extracting/integrating shared header and footer templates, connecting routes, rendering API data, and adapting the supplied pages for Flask/Jinja.

Course-provided instructional material, starter code, project structure, styling, assets, and template design are not claimed as my original work.
