# Day 35 — Weather API & Rain Alert

Day 35 of **Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp** focused on using APIs to retrieve weather information and triggering automated actions based on API data.

This project uses the OpenWeatherMap forecast API to check upcoming weather conditions and sends an email notification if rain is expected.

## What This Day Covers

- APIs and HTTP requests
- `requests`
- Query parameters
- JSON responses
- `response.raise_for_status()`
- Environment variables
- `.env` files with `python-dotenv`
- Iterating through API results
- Conditional logic
- SMTP email
- Automated notifications

## Project Structure

```text
Day 35/
└── main.py
```

A local `.env` file is used for API and email credentials and should not be committed to GitHub.

## How It Works

### 1. Load Credentials

The program loads the API key and email configuration from environment variables:

```python
load_dotenv()

API_KEY = os.getenv("API_KEY")

my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("EMAIL_PASSWORD")
send_to = os.environ.get("SEND_TO")
```

### 2. Request the Forecast

The OpenWeatherMap forecast API is queried using latitude, longitude, an API key, and a count of forecast entries.

The response is checked with:

```python
response.raise_for_status()
```

and converted to Python data with:

```python
weather_data = response.json()
```

### 3. Detect Rain

The program checks the weather ID in each returned forecast entry:

```python
for item in weather_data["list"]:
    if item["weather"][0]["id"] < 700:
        will_rain = True
```

If a matching weather condition is found, `will_rain` becomes `True`.

### 4. Send an Email

If rain is expected, the program connects to Gmail's SMTP server, starts TLS, authenticates, and sends an umbrella reminder.

The overall workflow is:

**Weather API → forecast data → rain detection → email notification**

## Concepts Practiced

- REST APIs
- HTTP GET requests
- JSON
- Query parameters
- API response validation
- Environment variables
- `python-dotenv`
- Nested dictionaries/lists
- Iteration
- Boolean state
- Conditional logic
- SMTP
- Email automation
- Credential management

## Development Notes

This project builds on the API concepts introduced in Day 33. Instead of simply retrieving and displaying information, the program now uses external data to make a decision and trigger an automated action.

## Security Note

API keys and email credentials are loaded from environment variables rather than being written directly into the source code.

The `.env` file should remain local and be excluded from version control.

## Course Attribution

The project concept, requirements, and learning objectives originate from **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

## Disclosure

This README was written with AI assistance. **The code attribution and implementation details reflect the work completed for the course project.**
