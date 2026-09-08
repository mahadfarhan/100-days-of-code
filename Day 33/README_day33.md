# Day 33 — APIs, HTTP Requests & ISS Overhead

Day 33 of **Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp** focused on working with APIs and using external data inside Python programs.

This day introduced HTTP requests, JSON responses, API parameters, dates and times, environment variables, email automation, and combining APIs with existing Python applications.

## What This Day Covers

- APIs and API endpoints
- HTTP GET requests with `requests`
- JSON responses
- Parsing nested JSON data
- Query parameters
- `response.raise_for_status()`
- `datetime`
- Environment variables and `.env` files
- `python-dotenv`
- Sending email with `smtplib`
- Combining multiple APIs
- Integrating API data into an existing Tkinter interface

## Project Structure

```text
Day 33/
├── exercises/
│   └── main.py
├── iss overhead/
│   ├── config.py
│   └── main.py
├── kanye quotes/
│   ├── background.png
│   ├── kanye.png
│   └── main.py
└── README.md
```

## API Exercises

The exercises introduced the basic workflow for working with web APIs:

1. Send a request using `requests`.
2. Check whether the request was successful.
3. Convert the response into Python data with `.json()`.
4. Extract the required information from the returned data.
5. Supply query parameters when an API requires additional information.

The exercises also use the Sunrise-Sunset API to retrieve sunrise and sunset information for a specified location.

## Kanye Quotes

The Kanye Quotes project was provided with the Tkinter interface and visual assets already set up.

My task was to integrate the external API into that existing interface and replace the placeholder quote text with live data returned by the API.

### API Integration

The program sends a GET request to:

```text
https://api.kanye.rest
```

and then:

1. Checks the response with `raise_for_status()`.
2. Converts the response to JSON.
3. Extracts the `quote` value.
4. Updates the existing Canvas text with the returned quote.

The API logic is:

```python
def get_quote():
    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()
    canvas.itemconfig(quote_text, text=response.json()["quote"])
```

This project therefore focused specifically on **connecting an existing GUI to an API**, rather than building the Tkinter interface itself.

## ISS Overhead

The ISS project combines multiple external services and Python features to determine whether the International Space Station is currently near a specified location and whether it is dark enough for it to potentially be visible.

### How It Works

The program:

1. Loads configuration values from environment variables.
2. Requests the ISS's current latitude and longitude.
3. Determines whether the ISS is within a defined range of the specified location.
4. Requests sunrise and sunset information from the Sunrise-Sunset API.
5. Compares the current time with sunrise and sunset.
6. If the ISS is nearby and it is nighttime, sends an email notification.

The project uses:

- `requests`
- Open Notify's ISS location API
- Sunrise-Sunset API
- `datetime`
- `smtplib`
- `python-dotenv`
- Environment variables

## Environment Variables

The ISS project keeps configuration and email credentials outside the main source code.

Values are loaded with:

```python
load_dotenv()
```

and retrieved with:

```python
os.environ.get(...)
```

This separates sensitive configuration from the program itself.

## Error Handling

API requests use:

```python
response.raise_for_status()
```

so unsuccessful HTTP responses raise an exception instead of being silently treated as successful requests.

## Concepts Practiced

- REST APIs
- HTTP GET requests
- `requests`
- JSON
- Dictionaries and nested data
- Query parameters
- API response validation
- `datetime`
- Environment variables
- `.env`
- `python-dotenv`
- SMTP
- Email automation
- Integrating external data into an existing GUI
- Combining multiple APIs

## Development Notes

Day 33 was a major expansion of the types of programs being built. Instead of relying mainly on local files and data, these projects communicate with external services and work with live information returned by APIs.

The Kanye Quotes project focused on API integration into a pre-built Tkinter interface, while the ISS project combines multiple APIs with time calculations, environment variables, and automated email.

This day also connects directly to the original motivation for learning Python: working with information available on the web. Instead of scraping HTML, APIs provide structured data directly in a format Python can consume.

## Course Attribution

The project concepts, exercises, APIs, project requirements, and the pre-built Tkinter interface/assets for the Kanye Quotes project originate from **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

## Disclosure

This README was written with AI assistance.

**For the Kanye Quotes project, the Tkinter interface and visual assets were provided by the course; I implemented the API integration and replaced the starter text with live quote data. Other Day 33 code reflects the implementation work completed during the course exercises and projects.**
