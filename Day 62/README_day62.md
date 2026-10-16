# Day 62 — Flask-WTF, Bootstrap & Coffee and WiFi Project

Day 62 of **100 Days of Code: The Complete Python Pro Bootcamp** builds on the Flask forms and templating concepts from Day 61 by creating a **Coffee & WiFi** web application for viewing and adding cafés.

The application uses Flask to handle page routes, Flask-WTF and WTForms to define and validate a café submission form, Bootstrap-Flask to style the interface, and a CSV file to store and display café information. Users can see café opening hours, location links, and ratings for coffee, Wi-Fi, and power outlets.

## Features

- Serves a homepage introducing the Coffee & WiFi directory
- Displays existing cafés in a Bootstrap-styled table
- Reads café information from `cafe-data.csv`
- Uses Jinja loops to generate the table rows and headers dynamically
- Converts café location URLs into clickable **Maps Link** entries
- Provides a form for submitting new cafés at `/add`
- Collects café name, location URL, opening and closing times, and three ratings
- Uses emoji-based dropdown choices for coffee, Wi-Fi, and power availability
- Validates required form fields and checks the location URL format
- Appends valid submissions to the CSV file without overwriting existing data
- Redirects to the add-café page after a successful submission
- Reuses a base template and Bootstrap styling across pages

## Technologies Used

- Python
- Flask
- Flask-WTF
- WTForms
- Bootstrap-Flask (`Bootstrap5`)
- Jinja2
- HTML
- CSS
- Python `csv` module
- CSV file storage

## Project Overview

### Flask Setup (`main.py`)

The application initializes Flask and Bootstrap-Flask:

```python
app = Flask(__name__)
app.config["SECRET_KEY"] = "..."
bootstrap = Bootstrap5(app)
```

The secret key is used by Flask-WTF for form security, including CSRF protection. The uploaded code sets a fixed key directly in `main.py`; for a deployed project, it should instead be loaded securely from an environment variable.

### Defining the Café Form

A `CafeForm` class inherits from `FlaskForm` and defines the information required for each café:

```python
class CafeForm(FlaskForm):
    cafe = StringField("Cafe name", validators=[DataRequired()])
    location_url = StringField(
        "Location URL", validators=[DataRequired(), URL()]
    )
    open_time = StringField("Open time", validators=[DataRequired()])
    closing_time = StringField("Closing time", validators=[DataRequired()])
```

Three `SelectField` inputs provide emoji-based ratings from no rating (`✘`) to five symbols:

- **Coffee quality:** ☕
- **Wi-Fi:** 💪
- **Power outlets:** 🔌

Each rating field uses `InputRequired()`. The form ends with a `SubmitField` button.

This demonstrates the difference between free-text fields and constrained dropdown inputs, as well as server-side form validation.

### Handling GET and POST Requests

The `/add` endpoint supports both displaying the form and processing its submission:

```python
@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        # Append the café details to the CSV file.
        ...
        return redirect(url_for("add_cafe"))
    return render_template("add.html", form=form)
```

On a GET request, the form is rendered. On a valid POST request, the submitted values are saved and the visitor is redirected back to `/add`. Invalid submissions do not get written to the CSV file.

### Saving Cafés to CSV

The program appends each validated submission to `cafe-data.csv`:

```python
with open("cafe-data.csv", mode="a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow([
        form.cafe.data,
        form.location_url.data,
        form.open_time.data,
        form.closing_time.data,
        form.coffee_rating.data,
        form.wifi_rating.data,
        form.power_outlet_rating.data,
    ])
```

Append mode (`"a"`) preserves existing café records. `csv.writer()` manages the CSV formatting, while `newline=""` prevents unwanted blank rows on platforms where newline handling differs. UTF-8 encoding supports the emoji ratings.

The CSV file contains seven columns:

| Column | Description |
| --- | --- |
| `Cafe Name` | Name of the café |
| `Location` | Link to its location |
| `Open` | Opening time |
| `Close` | Closing time |
| `Coffee` | Coffee rating |
| `Wifi` | Wi-Fi rating |
| `Power` | Power outlet rating |

### Reading and Displaying the Café Directory

The `/cafes` route reads the CSV file and passes the rows to its template:

```python
@app.route("/cafes")
def cafes():
    with open("cafe-data.csv", newline="", encoding="utf-8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=",")
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template("cafes.html", cafes=list_of_rows)
```

In `cafes.html`, Jinja iterates through those rows. The first row becomes the table header, and the remaining rows become café entries:

```jinja2
{% for cafe in cafes %}
    {% if loop.first %}
        <tr>
            {% for cafe_heading in cafe %}
                <th>{{ cafe_heading }}</th>
            {% endfor %}
        </tr>
    {% else %}
        <!-- Render each café's data -->
    {% endif %}
{% endfor %}
```

The template checks whether each cell begins with `http`. When it does, the value is rendered as a clickable **Maps Link** instead of displaying the raw URL.

The table uses Bootstrap's `table`, `table-dark`, `table-striped`, and `table-hover` classes.

### Templates and Styling

The pages share `base.html`, which loads Bootstrap CSS and the project's stylesheet:

```jinja2
{% extends 'base.html' %}
```

- `index.html` introduces the directory and links to the café list.
- `add.html` imports Bootstrap's `render_form` macro and renders the WTForms form.
- `cafes.html` displays the CSV data in a table.
- `base.html` defines reusable styling, title, and content blocks.

The add form is rendered using:

```jinja2
{% from 'bootstrap/form.html' import render_form %}
{{ render_form(form, novalidate=True) }}
```

The `novalidate=True` option leaves validation to the server-side Flask-WTF/WTForms workflow rather than relying on browser-native validation.

## Application Flow

```text
Start Flask application
        ↓
Visit homepage (/)
        ↓
Open café directory (/cafes)
        ↓
Read cafe-data.csv
        ↓
Render café table with Jinja

Visit add-café form (/add)
        ↓
Enter café details and ratings
        ↓
Submit POST request
        ↓
Validate form
        ↓
Valid? ── No → Render form again
   │
  Yes
   ↓
Append new café row to CSV
   ↓
Redirect to /add
        ↓
Updated café appears in /cafes
```

## Project Structure

```text
Day 62/
├── static/
│   └── css/
│       └── styles.css
├── templates/
│   ├── add.html
│   ├── base.html
│   ├── cafes.html
│   └── index.html
├── cafe-data.csv
├── main.py
└── requirements.txt
```

### `main.py`

Defines the `CafeForm`, initializes Flask and Bootstrap, serves the three routes, validates submissions, and reads/writes café records.

### `cafe-data.csv`

Stores the existing café directory and receives newly submitted entries.

### `templates/`

Contains the homepage, reusable base layout, café submission form, and café directory table.

### `static/css/styles.css`

Contains additional styles used alongside Bootstrap.

### `requirements.txt`

Lists the project's Python dependencies.

## Running the Project

Install the dependencies from the Day 62 folder:

```bash
pip install -r requirements.txt
```

Run the Flask app:

```bash
python main.py
```

Then open the local server URL, normally `http://127.0.0.1:5000/`.

Routes:

| URL | Purpose |
| --- | --- |
| `/` | Homepage |
| `/cafes` | Café directory |
| `/add` | Add a new café |

Run the program from the folder containing `cafe-data.csv`, since the application uses a relative path to that file.

## What I Learned

Day 62 brings together form handling, data validation, persistent file storage, and dynamic HTML rendering.

Key concepts included:

- Creating more complex forms with Flask-WTF
- Choosing appropriate WTForms field types
- Using `DataRequired()`, `InputRequired()`, and `URL()` validators
- Populating dropdowns with predefined choices
- Handling GET and POST requests in the same route
- Accessing validated inputs through `form.<field>.data`
- Using `validate_on_submit()` before saving user input
- Using `csv.writer()` to append rows to an existing file
- Reading CSV rows with `csv.reader()`
- Passing file data from Flask routes into Jinja templates
- Using `loop.first` and nested Jinja loops to build HTML tables
- Conditionally formatting CSV values as HTML links
- Rendering WTForms with Bootstrap-Flask macros
- Using template inheritance and reusable layouts
- Redirecting after successful POST requests

## Development Notes

This project extends the Day 61 login-form exercise into an application that stores user-submitted data and makes it available on another page.

The progression is:

**Flask-WTF form → input validation → CSV persistence → Jinja rendering → Bootstrap table**

Instead of only checking whether form values match an expected input, the application writes valid submissions to a file. The `/cafes` route then reads that same file to generate the directory, connecting form submission with persistent data display.

This is a course project using CSV-based storage rather than a database. The current implementation also uses a development secret key stored directly in the source code and Flask's debug server; these would need to be changed before production deployment.

## Course Attribution

The project concepts, exercises, and provided starter materials originate from **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

## Disclosure

This README was written with AI assistance. **Any code authored by me in this repository was written independently by me.**

Course-provided instructional material, starter code, project structures, assets, and example implementations are not claimed as my original work.
