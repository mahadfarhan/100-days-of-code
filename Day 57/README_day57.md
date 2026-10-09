# Day 57 — Jinja Templating & Blog Capstone Project

Day 57 of **100 Days of Code: The Complete Python Pro Bootcamp** builds on Flask routing and HTML templates by introducing **Jinja**, Flask's template engine for inserting Python-provided data into HTML.

The exercises demonstrate dynamic template variables, expressions, loops, conditional rendering, URL generation, and external API responses. The **Blog Capstone Project** applies these concepts to a multi-page blog that fetches posts from an API, displays them on a homepage, and opens individual articles using dynamic routes.

## Features

- Renders HTML templates with Flask's `render_template()`
- Passes Python values into Jinja templates
- Evaluates expressions and formats displayed values in HTML
- Uses Jinja loops and conditional statements
- Generates links with Flask's `url_for()`
- Fetches JSON data from external APIs using `requests`
- Uses Agify and Genderize to generate age and gender estimates from a name
- Loads an API key from an environment variable in the exercises
- Retrieves blog posts from an npoint JSON endpoint
- Displays a blog homepage with a card for each post
- Uses an integer URL parameter to select and render a full blog post
- Styles blog pages with a separate CSS stylesheet

## Technologies Used

- Python
- Flask
- Jinja2 templates
- HTML
- CSS
- `requests`
- `random`
- `datetime`
- `python-dotenv`
- `os` and environment variables
- REST APIs and JSON

## Exercises

### Dynamic Template Variables (`exercise/server.py`)

The homepage generates a random number and retrieves the current year, then passes both values into the HTML template:

```python
@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_year = dt.date.today().year
    return render_template("index.html", num=random_number, year=current_year)
```

Inside `templates/index.html`, Jinja's double braces display the supplied values:

```html
<h2>{{ 5 * 6 }}</h2>
<h3>Random number: {{ num }}</h3>
<p>© Copyright {{ year }}. Built by Mahad at Stellix Soft.</p>
```

This separates the logic that calculates values in Python from the HTML responsible for displaying them.

### Name-Based Prediction (`exercise/server.py`)

The `/guess/<name>` route accepts a name directly from the URL and sends it to the Agify and Genderize APIs:

```python
@app.route("/guess/<name>")
def guess(name):
    parameters = {"name": name, "apikey": APIKEY}

    response = requests.get("https://api.agify.io", params=parameters)
    response.raise_for_status()
    age_data = response.json()

    response = requests.get("https://api.genderize.io", params=parameters)
    response.raise_for_status()
    gender_data = response.json()

    return render_template(
        "guess.html",
        guess_name=name,
        age=age_data["age"],
        gender=gender_data["gender"]
    )
```

The API key is retrieved from an environment variable using `load_dotenv()` and `os.getenv("APIKEY")`. The `guess.html` template displays the result using expressions such as `{{ guess_name.title() }}`, `{{ gender }}`, and `{{ age }}`. These are API-based estimates, not verified demographic information.

### Jinja Loops, Conditionals & Links

The `/blog/<num>` exercise route fetches a list of posts from an npoint endpoint and sends the list to `blog.html`.

That template loops over posts, selects the post with ID `2`, and displays its title and subtitle:

```html
{% for blog_post in posts: %}
    {% if blog_post["id"] == 2: %}
        <h1>{{ blog_post["title"] }}</h1>
        <h2>{{ blog_post["subtitle"] }}</h2>
    {% endif %}
{% endfor %}
```

The exercise homepage also uses `url_for('get_blog', num=3)` to build a link to the blog route. In the uploaded exercise, the route accepts and prints `num`, but the template's filtering is hard-coded to post ID `2`.

## Blog Capstone Project (`Blog capstone project/main.py`)

The main project creates a styled blog with a post-listing page and individual post pages.

### Fetching Blog Data

The home route requests the blog-post data from npoint, validates the HTTP response, converts the JSON into Python data, and passes the results into `index.html`:

```python
@app.route("/")
def home():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    response.raise_for_status()

    all_posts = response.json()

    return render_template("index.html", posts=all_posts)
```

### Rendering Post Cards

The homepage uses a Jinja `for` loop to create a card for each post:

```html
{% for post in posts: %}
<div class="content">
    <div class="card">
        <h2>{{ post["title"] }}</h2>
        <p class="text">{{ post["title"] }}</p>
        <a href="{{ url_for('blog_post', blog_id=post['id']) }}">Read</a>
    </div>
</div>
{% endfor %}
```

Each **Read** link passes the selected post's ID into Flask's `blog_post` endpoint. In the uploaded homepage template, the card paragraph repeats the post title.

### Dynamic Blog Post Pages

A typed route receives the selected post ID, fetches the full list of posts, and returns the matching post to the template:

```python
@app.route("/post/<int:blog_id>")
def blog_post(blog_id):
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    response.raise_for_status()

    all_posts = response.json()

    for post in all_posts:
        if post["id"] == blog_id:
            return render_template("post.html", post=post, id=int(blog_id))
```

The `post.html` template displays the selected post's **title**, **subtitle**, and **body** using Jinja expressions:

```html
<h1>{{ post["title"] }}</h1>
<h2>{{ post["subtitle"] }}</h2>
<p>{{ post["body"] }}</p>
```

Using `<int:blog_id>` ensures Flask accepts an integer for the route parameter. The uploaded version does not explicitly return a 404 response if no matching post is found.

### Blog Styling

The project keeps CSS in `static/css/styles.css`, separate from the HTML templates. The provided stylesheet styles the page background, blue header, centered white post cards, typography, card shadows, and fixed footer. The templates also load the Raleway font from Google Fonts.

## Application Flow

```text
Start Flask application
        ↓
Visit homepage (/)
        ↓
Fetch blog posts from npoint
        ↓
Parse JSON response
        ↓
Render index.html with posts
        ↓
Loop through posts and display cards
        ↓
Click "Read" on a post
        ↓
Navigate to /post/<blog_id>
        ↓
Fetch post data and find matching ID
        ↓
Render post.html with title, subtitle, and body
```

## Project Structure

```text
Day 57/
├── exercise/
│   ├── .env
│   ├── server.py
│   └── templates/
│       ├── index.html
│       ├── guess.html
│       └── blog.html
└── Blog capstone project/
    ├── main.py
    ├── static/
    │   └── css/
    │       └── styles.css
    └── templates/
        ├── index.html
        └── post.html
```

### `exercise/server.py`

Demonstrates dynamic template values, environment variables, API requests, name-based estimates, and Flask URL routing.

### `Blog capstone project/main.py`

Contains the Flask application, API-based blog-data retrieval, homepage route, and dynamic individual-post route.

### `templates/` and `static/css/`

Contain the Jinja HTML templates and external blog stylesheet.

## Running the Projects

Install the dependencies:

```bash
pip install flask requests python-dotenv
```

To run the exercises, create a local `exercise/.env` file with the required API key (if using a key):

```text
APIKEY=your_api_key_here
```

Run the exercise app from its directory:

```bash
python server.py
```

Or run the blog capstone from its own directory:

```bash
python main.py
```

Open the local address printed by Flask, typically `http://127.0.0.1:5000/`. The exercise provides `/guess/<name>` and `/blog/<num>` routes; the capstone provides `/post/<blog_id>` routes.

Keep `.env` files out of version control. Run only one application on the default Flask port at a time unless the ports are changed. `debug=True` is intended for local development.

## What I Learned

Day 57 builds on the previous Flask lessons by moving from mostly static HTML pages to templates populated with live Python data.

Key concepts included:

- `render_template()` passes data from Flask routes into HTML pages
- Jinja's `{{ ... }}` syntax evaluates and displays template expressions
- Jinja's `{% ... %}` syntax supports loops and conditions
- `url_for()` builds links using Flask endpoint names and parameters
- External APIs can provide data for dynamically generated pages
- `response.raise_for_status()` detects unsuccessful HTTP responses
- `response.json()` converts JSON responses into Python data structures
- Environment variables can keep API keys outside source code
- Dynamic route parameters can identify a specific blog post
- Multiple pages can share a stylesheet while displaying different data
- The same HTML template can render different content depending on which data Flask supplies

## Development Notes

Day 57 connects the separate concepts of Flask, API requests, Jinja, and CSS into a basic multi-page website.

The progression is:

**Flask routing → Jinja variables → loops and conditions → API data → dynamic links → individual post pages**

The exercises show how Python values and external API results can appear inside HTML. The capstone then uses those techniques to build a blog where one template renders multiple post previews and another renders a selected article.

The project currently fetches blog data again for each individual post request. Additional improvements could include handling unmatched post IDs with a 404 response, and reusing fetched data. These are potential improvements, not features claimed as implemented.

## Course Attribution

The project concepts and exercises originate from **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

## Disclosure

This README was written with AI assistance. **Any code authored by me in this repository was written independently by me.**

Course-provided instructional material, starter code, project structures, assets, and example implementations are not claimed as my original work.
