# Day 40 — Flight Deal Finder: User Notifications & Price Updates

Day 40 of **Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp** continued the Flight Deal Finder project from Day 39.

This version expands the application to support multiple users, update stored target prices when cheaper flights are found, handle flight availability with different stop configurations, and include stop information in automated email notifications.

## What This Day Covers

- Extending an existing multi-module application
- REST APIs
- HTTP `GET` and `PUT` requests
- API authentication
- Request headers
- JSON data
- Environment variables
- `.env` files with `python-dotenv`
- `requests_cache`
- Object-oriented programming
- Multiple Python modules
- Data transformation
- Conditional logic
- API response handling
- Multiple email recipients
- BCC email delivery
- Updating stored data through an API
- Automated notifications

## Project Structure

```text
Day 40/
├── data_manager.py
├── flight_data.py
├── flight_search.py
├── main.py
└── notification_manager.py
```

API credentials and email configuration are loaded from environment variables and should not be committed to GitHub.

## Flight Deal Finder

Day 40 builds directly on the modular Flight Deal Finder created on Day 39.

The application now works with two types of spreadsheet data:

- Destination and target-price information
- User email addresses

The program searches for flights to each destination, identifies the cheapest qualifying flight, compares the price against the stored target price, updates the stored price when a cheaper flight is found, and sends a notification to the configured users.

The overall workflow is:

**Spreadsheet → destinations & users → flight search → cheapest flight → price comparison → update spreadsheet → email notification**

## Application Architecture

The project continues to separate responsibilities across several modules.

### `DataManager`

`DataManager` handles communication with the Sheety API.

It retrieves destination/price data and user email addresses, and can update a destination's stored lowest price using a `PUT` request.

This keeps spreadsheet retrieval and modification inside `DataManager`.

### `FlightSearch`

`FlightSearch` handles communication with SerpAPI.

The search parameters include:

- Departure airport
- Destination airport
- Travel duration
- Number of stops
- Search engine
- API key

The departure airport remains:

```text
ISB
```

The destination IATA code is supplied dynamically from the spreadsheet.

### Flight Availability

The application includes a separate method for checking whether qualifying flights exist.

It first searches using one stop and falls back to a broader stop configuration if no flights are returned.

```python
def check_flight_exists(self, arrival_id):
    result = self.get_data(arrival_id, 1)

    if not result.get("flights"):
        result = self.get_data(arrival_id, 3)

    return result
```

## `FlightData`

`FlightData` processes the raw flight-search response.

It searches through the returned flights for the one marked as the cheapest.

In addition to the price, it determines the number of stops and returns a human-readable description such as:

- `nonstop`
- `1 stop`
- `2 stops`

This information is passed to the notification system.

## `NotificationManager`

`NotificationManager` handles automated email delivery.

Email credentials are loaded from environment variables, and the email is sent through Gmail's SMTP server using TLS.

The notification supports multiple recipients through BCC and includes:

- Destination city
- Flight price
- Number of stops

## Main Program Flow

`main.py` coordinates the application's components.

The program:

1. Retrieves destination and user data.
2. Checks whether a qualifying flight exists for each destination.
3. Creates a `FlightData` object from the response.
4. Finds the cheapest flight and its number of stops.
5. Compares the flight price with the stored target price.
6. Updates the spreadsheet with the new lower price.
7. Sends an email notification to the configured users.

The central logic is:

```python
if cheapest_flight_price < item["lowestPrice"]:
    data_manager.update_price(cheapest_flight_price, item["id"])
    notification_manager.send_email(
        item["city"],
        cheapest_flight_price,
        cheapest_flight_stops,
        user_emails_list
    )
```

## API Integrations

The project combines several external services.

### Sheety

Used to:

- Retrieve destination and target-price data
- Retrieve user email addresses
- Update stored lowest prices

### SerpAPI

Used to search Google Travel flight information and determine available flights, prices, and stop information.

### Gmail SMTP

Used to send automated notifications to the collected user email addresses.

## Caching

The project uses `requests_cache` for API requests.

Separate cached sessions are used for Sheety and SerpAPI requests.

The generated SQLite cache files are runtime data and are excluded from version control.

## Authentication & Configuration

Sensitive configuration is loaded from environment variables using `python-dotenv`.

Examples include:

```python
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
SHEETY_PRICES_ENDPOINT = os.getenv("SHEETY_PRICES_ENDPOINT")
SHEETY_USERS_ENDPOINT = os.getenv("SHEETY_USERS_ENDPOINT")
SERP_API = os.getenv("SERP_API_KEY")
```

Email credentials are also loaded from environment variables.

This keeps authentication credentials separate from the source code.

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
- HTTP `PUT` requests
- API authentication
- Request headers
- JSON
- `requests`
- `requests_cache`
- Environment variables
- `python-dotenv`
- Classes and objects
- Multiple modules
- Separation of responsibilities
- Data extraction
- Data transformation
- Conditional logic
- API response validation
- SMTP
- BCC email delivery
- Automated notifications
- Updating remote data
- Data pipelines

## Development Notes

Day 40 extends the architecture established on Day 39 rather than starting a completely separate application.

The project now has a more complete feedback loop:

**Search → compare → update → notify**

When a cheaper flight is discovered, the new price is written back to the spreadsheet. The notification also provides additional information about whether the flight is nonstop or requires stops.

This combines API retrieval, API modification, data processing, and automated communication within the same modular application.

## Security Note

API keys, Bearer tokens, and email credentials are loaded through environment variables rather than being stored directly in the Python source code.

Runtime cache databases are excluded from version control.

## Course Attribution

The project concepts and exercises originate from **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

## Disclosure

This README was written with AI assistance. **Any code authored by me in this repository was written independently by me.**
