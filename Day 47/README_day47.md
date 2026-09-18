# Day 47 — Amazon Price Tracker

Day 47 of **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu combined web scraping with automated email notifications to create a simple **price tracker**.

The program checks the price of an item, compares it against a target price, and sends an email notification when the item becomes cheap enough to buy.

## What I Learned

- Web scraping with `requests`
- Parsing HTML with BeautifulSoup
- Using HTTP request headers
- Loading configuration from environment variables
- Creating emails with `EmailMessage`
- Sending email through SMTP
- Using Gmail's SMTP server
- Starting a TLS-encrypted SMTP connection
- Automating actions based on scraped data
- Combining web scraping with email automation

## Project

### Amazon Price Tracker

The project retrieves an item's price from a webpage and checks whether it has dropped below a predefined target.

Email configuration is loaded from environment variables:

```python
load_dotenv()

my_email = os.getenv("MY_EMAIL")
my_password = os.getenv("MY_PASSWORD")
send_to = os.getenv("SEND_TO")
```

This keeps credentials outside the Python source code.

## Scraping the Price

The program requests the item webpage using `requests` and includes browser-style HTTP headers:

```python
response = requests.get(
    "https://appbrewery.github.io/instant_pot/",
    headers=headers
)
response.raise_for_status()
```

The returned HTML is then parsed with BeautifulSoup:

```python
amazon_website = response.text

soup = BeautifulSoup(amazon_website, "html.parser")
```

The price is extracted using a CSS selector:

```python
price = float(
    soup.select_one(".twisterSwatchPrice")
    .getText()
    .strip()
    .replace("$", "")
)
```

The scraped text is cleaned and converted to a `float` so it can be compared numerically with the target price.

## Email Notification

The project uses Python's `EmailMessage` class to construct the notification:

```python
msg = EmailMessage()

msg["Subject"] = "Price of item cheaper than target!"
msg["From"] = my_email
msg["To"] = send_to
msg.set_content(
    "Price of the item you want is cheap enough for you to buy!"
)
```

The email is sent only when the price falls below the target:

```python
if price < 100:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.send_message(msg)
```

The SMTP connection is upgraded to TLS before authentication and sending the message.

## Project Workflow

```text
Request item webpage
        ↓
Receive HTML
        ↓
Parse HTML with BeautifulSoup
        ↓
Extract price
        ↓
Convert price to a number
        ↓
Compare with target
        ↓
If price is low enough
        ↓
Create email
        ↓
Connect to SMTP server
        ↓
Send notification
```

This turns a simple web scraper into an automated notification system.

## Project Structure

```text
Day 47/
├── .cache
├── .env
└── main.py
```

### `.env`

The `.env` file stores sensitive configuration such as:

- Email address
- Email password
- Recipient email address

These values should remain private and should not be committed to version control.

### `.cache`

Local cache data should also remain outside version control where appropriate.

## Concepts Practiced

### Web Scraping

- `requests.get()`
- HTTP headers
- `response.text`
- `raise_for_status()`
- BeautifulSoup
- CSS selectors
- `.select_one()`
- `.getText()`
- String cleaning
- Numeric type conversion

### Environment Variables

- `python-dotenv`
- `load_dotenv()`
- `os.getenv()`
- Keeping credentials outside source code

### Email

- `EmailMessage`
- SMTP
- Gmail SMTP
- `starttls()`
- SMTP authentication
- Sending messages programmatically

### Python

- Variables
- String manipulation
- Type conversion
- Conditional statements
- Context managers
- Third-party libraries

## Development Notes

Day 47 builds on the web-scraping concepts introduced earlier in the course and combines them with automated email communication.

The progression is:

**Webpage → scrape data → process data → make a decision → trigger an automated action**

Unlike the earlier scraping projects, the scraped information is not simply displayed or saved. It determines whether the program performs another action: sending an email notification.

This is another step toward building small automated applications that interact with external services.

## Course Attribution

The project concepts and exercises originate from **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

## Disclosure

This README was written with AI assistance. **Any code authored by me in this repository was written independently by me.**
