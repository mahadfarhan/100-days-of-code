# Day 36 — Stock News Alert

Day 36 of **Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp** focused on combining multiple APIs, processing financial data, and automating email notifications.

This project retrieves live stock-market data from Alpha Vantage, calculates the percentage movement between the two most recent trading days, and—if the absolute movement reaches at least 5%—retrieves related news articles from NewsAPI and sends an email summary.

## What This Day Covers

- Multiple API integrations
- HTTP requests with `requests`
- API query parameters
- JSON data
- Processing nested API responses
- Percentage-change calculations
- Conditional logic
- Environment variables
- `.env` files with `python-dotenv`
- `EmailMessage`
- SMTP email automation
- Local JSON testing
- Combining data from multiple external services

## Project Structure

```text
Day 36/
├── .env
├── local_json_for_testing.json
└── main.py
```

The `.env` file contains API credentials and email configuration and should not be committed to GitHub.

## Stock News Alert

The project is configured around a stock symbol and company name:

```python
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
```

The program monitors the stock's recent daily price movement and only proceeds to the news and email stage when the movement reaches the configured threshold.

## 1. Retrieve Live Stock Data

The program uses Alpha Vantage's daily time-series endpoint:

```python
params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": os.getenv("APIKEY"),
}

response = requests.get(
    "https://www.alphavantage.co/query?",
    params=params
)
response.raise_for_status()

tsla_data = response.json()
```

The current implementation uses the **live API response** as its normal data source.

A local JSON workflow is also kept in the code as commented-out testing code:

```python
# with open("local_json_for_testing.json", "w") as file:
#     json.dump(tsla_data, file)

# with open("local_json_for_testing.json", "r") as file:
#     tsla_data = json.load(file)
```

This allows a captured API response to be used during development without repeatedly making external requests.

## 2. Calculate Stock Movement

The program extracts the two most recent daily entries and retrieves their closing prices.

The percentage change is calculated with:

```python
price_change = ((price_list[0] - price_list[1]) / price_list[1]) * 100
```

The direction is determined before converting the value to an absolute percentage:

```python
if price_change < 0:
    arrow = "🔻"
else:
    arrow = "🔺"

price_change = abs(price_change)
```

This preserves whether the stock moved upward or downward while allowing the threshold check to use the magnitude of the movement.

## 3. Check the 5% Threshold

News is only retrieved when the absolute stock-price movement is at least 5%:

```python
if price_change >= 5:
```

This prevents the program from sending unnecessary news emails when the stock has only experienced a smaller daily movement.

## 4. Retrieve Related News

When the 5% threshold is reached, the program queries NewsAPI for recent articles related to the configured company:

```python
news_params = {
    "q": COMPANY_NAME,
    "sortBy": "publishedAt",
    "apiKey": os.getenv("NEWSAPI"),
}
```

The first three returned articles are selected.

For each article, the program extracts:

- Headline
- Brief description

These are combined into the email body.

## 5. Send the Email

The email is created using Python's `EmailMessage`:

```python
msg = EmailMessage()
```

The subject includes:

- The stock symbol
- An upward or downward indicator
- The percentage movement

The email is then sent through Gmail's SMTP server using TLS:

```python
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.send_message(msg)
```

## Overall Workflow

**Alpha Vantage → stock prices → percentage movement → 5% threshold → NewsAPI → three recent articles → email notification**

The important feature is that the second API is only contacted when the first API indicates that a sufficiently large price movement has occurred.

## Concepts Practiced

- REST APIs
- Multiple API integrations
- `requests`
- Query parameters
- JSON
- Nested dictionaries and lists
- File I/O
- Percentage calculations
- Absolute values
- Conditional logic
- Environment variables
- `python-dotenv`
- `EmailMessage`
- SMTP
- Automated email
- Data transformation
- Local API-response testing
- Combining external data sources

## Development Notes

A local JSON response is included as a testing option, but the current implementation retrieves stock data directly from Alpha Vantage.

The project demonstrates a more complete automation pipeline than the previous API projects:

1. Retrieve live data.
2. Process the data.
3. Determine whether an event meets a defined threshold.
4. Retrieve additional information only when relevant.
5. Combine the results.
6. Automatically deliver the information by email.

## Security Note

API keys and email credentials are loaded through environment variables rather than being stored directly in the Python source code.

The `.env` file should remain local and be excluded from version control.

## Course Attribution

The project concepts and exercises originate from **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

## Disclosure

This README was written with AI assistance. **Any code authored by me in this repository was written independently by me.**
