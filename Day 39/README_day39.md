# Day 39 — Flight Deal Finder

Day 39 of **Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp** focused on building a larger, modular application by combining multiple APIs, data processing, caching, object-oriented programming, and automated email notifications.

This project searches for flight deals from a configured departure airport, compares returned prices against target prices stored in a spreadsheet, and sends an email notification when a cheaper flight is found.

## What This Day Covers

- REST APIs
- Multiple API integrations
- HTTP `GET` requests
- API parameters
- JSON responses
- API authentication
- Request headers
- Environment variables
- `.env` files with `python-dotenv`
- `requests_cache`
- Object-oriented programming
- Multiple Python modules
- Data transformation
- Conditional logic
- Automated email notifications
- Spreadsheet API integration
- Separation of application responsibilities

## Project Structure

```text
Day 39/
├── data_manager.py
├── flight_data.py
├── flight_search.py
├── main.py
└── notification_manager.py
```

Runtime-generated files such as the API cache databases and sensitive configuration files are excluded from version control.

## Flight Deal Finder

The application uses a spreadsheet as the source of desired destinations and target prices.

The main program retrieves the destination data, searches for flight information for each destination, identifies the cheapest qualifying flight, compares that price against the target price, and sends an email if a deal is found.

The overall workflow is:

**Spreadsheet → destination data → flight search API → cheapest flight → price comparison → email notification**

## Application Architecture

The project is divided into separate classes/modules, with each component responsible for a specific part of the application.

### `DataManager`

`DataManager` handles retrieving destination and target-price data from the Sheety API.

It creates a cached HTTP session, authenticates the request using the configured Bearer token, sends the request to the Sheety endpoint, and returns the resulting JSON data.

This keeps spreadsheet-related API logic separate from the rest of the application.

### `FlightSearch`

`FlightSearch` handles searching for flights through SerpAPI.

The search request includes parameters such as:

- Departure airport
- Destination airport
- Travel duration
- Search type
- API key

The current departure airport is:

```text
ISB
```

The destination IATA code is supplied dynamically from the spreadsheet data.

A cached session is used for flight-search requests.

### `FlightData`

`FlightData` handles processing the returned flight information.

The raw API response is passed into the class, which searches the returned flights for the flight marked as the cheapest and returns its price.

This keeps flight-data processing separate from the API request itself.

### `NotificationManager`

`NotificationManager` handles email notifications.

Email credentials are loaded from environment variables, and messages are sent through Gmail's SMTP server using TLS.

The notification contains the destination city and detected flight price.

## Main Program Flow

The main program creates instances of the application's components:

```python
data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()
```

It then retrieves the destination data and processes each destination.

For each destination, the program:

1. Retrieves flight information.
2. Creates a `FlightData` object from the response.
3. Finds the cheapest qualifying flight.
4. Compares the price against the destination's stored target price.
5. Sends an email if the flight is cheaper than the target.

This keeps `main.py` focused primarily on coordinating the different components rather than implementing every operation itself.

## API Integrations

The project combines multiple external services.

### Sheety

Used to retrieve the spreadsheet containing destination information and target prices.

### SerpAPI

Used to search Google Travel flight information using destination IATA codes.

### Gmail SMTP

Used to send automated notifications when a qualifying flight deal is found.

## Caching

The project uses `requests_cache` for API requests.

Separate cached sessions are created for the Sheety and SerpAPI requests.

The resulting SQLite cache files are runtime-generated files and are excluded from version control.

## Authentication & Configuration

Sensitive configuration is loaded from environment variables using `python-dotenv`.

Examples include:

```python
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
SERP_API = os.getenv("SERP_API_KEY")
```

Email credentials are also loaded from environment variables by `NotificationManager`.

This keeps credentials separate from the source code.

## Error Handling

API responses use:

```python
response.raise_for_status()
```

so unsuccessful HTTP responses raise an exception rather than allowing the program to continue silently.

## Concepts Practiced

- REST APIs
- Multiple API integrations
- HTTP `GET` requests
- API parameters
- JSON
- API authentication
- Request headers
- Environment variables
- `python-dotenv`
- `requests_cache`
- Classes and objects
- Multiple modules
- Separation of responsibilities
- Data extraction
- Data transformation
- Conditional logic
- SMTP
- Automated email
- Spreadsheet APIs
- Data pipelines

## Development Notes

Day 39 represents a significant increase in project complexity compared with the earlier API exercises.

Instead of having one script perform every task, the application is divided into components with distinct responsibilities:

**DataManager** → spreadsheet data  
**FlightSearch** → flight API  
**FlightData** → flight-data processing  
**NotificationManager** → email  
**main.py** → application orchestration

This provides practical experience with organizing a larger Python application into separate modules and using classes to encapsulate related functionality.

## Security Note

API keys, Bearer tokens, and email credentials are loaded through environment variables rather than being stored directly in the Python source code.

Runtime cache databases are also excluded from version control.

## Course Attribution

The project concepts and exercises originate from **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

## Disclosure

This README was written with AI assistance. **Any code authored by me in this repository was written independently by me.**
