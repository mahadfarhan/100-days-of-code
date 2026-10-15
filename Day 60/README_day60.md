# Day 60 — Flask Forms, POST Requests & Contact Form Emails

Day 60 of **100 Days of Code: The Complete Python Pro Bootcamp** focuses on handling HTML form submissions in Flask and connecting a contact form to an email-sending workflow.

The exercises introduce `GET` and `POST` requests, Flask's `request.form`, and conditional Jinja rendering. The main project extends the blog from the previous day with a working contact form that collects a visitor's details and sends them via Gmail's SMTP server.

## Features

- Handles form submissions using Flask routes and HTTP `POST` requests
- Reads submitted form values with `request.form`
- Uses Jinja conditions to change a page after form submission
- Connects a contact form to a Flask backend
- Accepts both `GET` and `POST` requests at the `/contact` route
- Sends contact messages through Gmail SMTP with `smtplib`
- Establishes an encrypted SMTP connection using `starttls()`
- Loads email credentials and the destination address from environment variables
- Displays a confirmation heading after a message is sent
- Preserves the blog's API-powered post listings and individual post pages
- Reuses shared header and footer templates across the blog

## Technologies Used

- Python
- Flask
- Jinja2
- HTML forms
- HTTP `GET` and `POST`
- `requests`
- `smtplib`
- `python-dotenv`
- `os`
- Gmail SMTP
- Bootstrap / Start Bootstrap's Clean Blog theme

## Exercises

### HTML Forms (`html-forms/main.py` and `html-forms/templates/index.html`)

The first exercise demonstrates how a Flask application receives submitted form data.

The home page renders a form until a submission has been made:

```python
@app.route("/")
def home():
    submitted = False
    return render_template("index.html", submitted=submitted)
```

The HTML form sends its inputs to a separate endpoint:

```html
<form action="{{ url_for('receive_data') }}" method="post">
    <input type="text" name="username" placeholder="name">
    <input type="text" name="password" placeholder="password">
    <button type="submit">Ok</button>
</form>
```

The `/login` route accesses the submitted values through `request.form`:

```python
@app.route("/login", methods=["POST"])
def receive_data():
    submitted = True
    username = request.form["username"]
    password = request.form["password"]
    print(request.form)
    return render_template(
        "index.html", username=username, password=password, submitted=submitted
    )
```

A Jinja `{% if %}` statement decides whether to show the form or the submitted values. This is a form-handling demonstration, **not** a secure login system: the example prints form data and displays the entered password as plain text.

## Blog Project — Functional Contact Form

### Flask Routes (`Blog project/main.py`)

The blog continues to serve its existing routes:

| Route | Method(s) | Purpose |
| --- | --- | --- |
| `/` | `GET` | Displays posts retrieved from an npoint JSON endpoint |
| `/about` | `GET` | Displays the About page |
| `/contact` | `GET`, `POST` | Displays the contact form or processes a submission |
| `/post/<int:index>` | `GET` | Displays the selected blog post |

Blog data is loaded using `requests` and rendered into the existing Jinja templates. The principal addition for Day 60 is processing contact form submissions.

### Handling GET and POST

The contact route uses the request method to decide which action to take:

```python
@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "GET":
        return render_template("contact.html", submitted=False)
    elif request.method == "POST":
        # Connect to Gmail and send the submitted message.
        return render_template("contact.html", submitted=True)
```

- **GET:** renders the contact page with its normal heading.
- **POST:** reads the submitted form fields, sends an email, and renders a success heading if sending finishes without an exception.

In `contact.html`, the form is connected to the route with:

```html
<form id="contactForm" name="sentMessage" action="{{ url_for('contact') }}" method="post">
```

The fields use `name` attributes (`name`, `email`, `phone`, and `message`) so that Flask can retrieve their values.

### SMTP Email Delivery

The application loads email settings from a local `.env` file:

```python
load_dotenv()

my_email = os.getenv("MY_EMAIL")
password = os.getenv("EMAIL_PASSWORD")
send_to = os.getenv("SEND_TO")
```

The `POST` handler establishes an SMTP connection, starts TLS, authenticates, and sends the submitted details:

```python
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
```

This integrates form processing with a practical action: delivering a visitor's contact information to an inbox. The `Subject:` header appears before the blank line separating email headers from its body.

### Conditional Confirmation

After email submission, Flask renders `contact.html` with `submitted=True`. The template then changes the page heading:

```html
{% if submitted: %}
<h1>Successfully sent your message</h1>
{% else: %}
<h1>Contact Me</h1>
{% endif %}
```

If SMTP authentication or delivery raises an exception, the application does not reach this success response; there is no custom error-handling page in the supplied implementation.

## Application Flow

```text
Visitor opens /contact
         ↓
Flask receives GET request
         ↓
Render contact form (submitted=False)
         ↓
Visitor enters name, email, phone, and message
         ↓
Form sends POST request to /contact
         ↓
Flask reads request.form fields
         ↓
Connect to Gmail SMTP on port 587
         ↓
Start TLS and authenticate
         ↓
Send formatted email to destination address
         ↓
Render contact page (submitted=True)
         ↓
Display success heading
```

## Project Structure

```text
Day 60/
├── Blog project/
│   ├── static/
│   │   ├── assets/
│   │   │   ├── img/
│   │   │   └── favicon.ico
│   │   ├── css/
│   │   │   └── styles.css
│   │   └── js/
│   │       └── scripts.js
│   ├── templates/
│   │   ├── about.html
│   │   ├── contact.html
│   │   ├── footer.html
│   │   ├── header.html
│   │   ├── index.html
│   │   └── post.html
│   ├── .env                  # Local secrets; do not commit
│   ├── main.py
│   └── requirements.txt
└── html-forms/
    ├── templates/
    │   └── index.html
    └── main.py
```

### `Blog project/main.py`

Contains the blog routes, remote post-data retrieval, contact form GET/POST processing, and SMTP email sending.

### `Blog project/templates/contact.html`

Defines the contact form and uses a Jinja condition to change the heading after successful submission.

### `html-forms/main.py`

Demonstrates how Flask receives POST form data and passes the submitted values into a rendered template.

## Running the Projects

Install the dependencies for the blog application:

```bash
pip install Flask==2.3.2 requests==2.31.0 python-dotenv
```

The supplied `requirements.txt` lists Flask and Requests; `python-dotenv` is also required by `main.py` but is not currently listed in that file.

Create a local `.env` file inside `Blog project/` with your own values:

```dotenv
MY_EMAIL=your_address@gmail.com
EMAIL_PASSWORD=your_gmail_app_password
SEND_TO=recipient@example.com
```

Use an appropriate Gmail app password if your account supports it; do not store your regular Google password in source code. **Do not commit `.env` to GitHub.** Add it to `.gitignore`.

From the `Blog project` directory:

```bash
python main.py
```

The blog is configured to run at `http://127.0.0.1:5001/`; visit `/contact` to test the form.

To run the separate HTML forms exercise, navigate to `html-forms/` and run:

```bash
python main.py
```

Its Flask development server normally runs at `http://127.0.0.1:5000/`. The two projects use different default ports in the supplied code.

## What I Learned

Day 60 builds on Flask routing and Jinja templating by allowing a website to **receive and process user input**, rather than simply display dynamic data.

Key concepts included:

- The difference between `GET` and `POST` requests
- Setting HTML form `action` and `method` attributes
- Mapping input `name` attributes to values in `request.form`
- Enabling multiple HTTP methods on one Flask route
- Using conditional rendering to reflect submission status
- Loading sensitive configuration through environment variables
- Opening SMTP connections and upgrading them with TLS
- Authenticating and sending emails using Python's `smtplib`
- Integrating a provided frontend template with custom Flask backend logic
- Keeping authentication credentials outside committed project files

## Development Notes

This lesson extends the previous blog implementation from **rendering content** to **responding to submitted data**:

**HTML form → HTTP POST → Flask `request.form` → SMTP email → confirmation page**

The HTML forms exercise demonstrates the basic mechanics of submission. The blog project then applies those mechanics to a contact page, connecting a visitor-facing form to email delivery.

**Scope of my work:** Much of the blog's HTML, CSS, JavaScript, and theme layout came from the provided starter project. I implemented the Flask form wiring, `GET`/`POST` handling, SMTP configuration and message-sending logic, and the integration needed to display submission feedback. The course's starter materials and design are not presented as original work.

**Development limitation:** These are learning projects running with Flask's development server and `debug=True`. The blog form does not include production-oriented protections such as server-side validation, spam prevention, CSRF protection, or custom SMTP error handling. The exercise's password field is intentionally not a real authentication implementation.

## Course Attribution

The exercises and project concepts originate from **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

The blog uses the **Clean Blog** theme from **Start Bootstrap**, with starter HTML, CSS, JavaScript, imagery, and other provided project assets.

## Disclosure

This README was written with AI assistance. **Any code authored by me in this repository was written independently by me.**

Course-provided instructional material, starter code, project structures, assets, and example implementations are not claimed as my original work.
