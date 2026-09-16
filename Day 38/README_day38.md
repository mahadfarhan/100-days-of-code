# Day 38 — Workout Tracker

Day 38 of **Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp** focused on combining multiple APIs to create an automated workout-tracking application.

This project accepts natural-language descriptions of exercise, sends them to an exercise API to extract structured workout information, and then records the resulting data in a spreadsheet through the Sheety API.

## What This Day Covers

- Multiple API integrations
- HTTP `POST` requests
- API authentication
- Request headers
- JSON request bodies and responses
- Environment variables
- `.env` files with `python-dotenv`
- Data extraction and transformation
- `datetime`
- Spreadsheet API integration
- Chaining API requests
- Error handling

## Project Structure

```text
Day 38/
└── main.py
```

API credentials and other configuration values are stored in environment variables and should not be committed to GitHub.

## Workout Tracker

The program allows the user to describe their exercise in natural language.

For example:

```text
What did you do today? Ran for 30 minutes
```

The description is sent to the exercise API, which converts the natural-language input into structured workout information.

That information is then formatted and sent to a Sheety endpoint to be recorded in a workout spreadsheet.

## How It Works

### 1. Load API Credentials

The program loads its API credentials and Sheety configuration using `python-dotenv`:

```python
load_dotenv()

X_APP_ID = os.getenv("X-APP-ID")
X_APP_KEY = os.getenv("X-APP-KEY")
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
```

This keeps authentication credentials out of the source code.

### 2. Collect Natural-Language Exercise Input

The user provides a description of their exercise:

```python
query = input("What did you do today? ")
```

The query is sent to the exercise API along with the required information:

```python
exercise_params = {
    "query": query,
    "weight_kg": 45,
    "age": 22,
    "gender": "male"
}
```

### 3. Request Exercise Data

The program sends a `POST` request to the exercise endpoint:

```python
response = requests.post(
    url=exercise_endpoint,
    json=exercise_params,
    headers=exercise_headers
)
response.raise_for_status()
data = response.json()
```

The API response provides structured information about the exercise.

### 4. Transform the API Response

The program extracts the relevant fields from the API response and formats them for the spreadsheet:

```python
sheety_params = {
    "workout": {
        "date": today.strftime("%d/%m/%Y"),
        "time": today.strftime("%H:%M:%S"),
        "exercise": data["exercises"][0]["name"],
        "duration": data["exercises"][0]["duration_min"],
        "calories": data["exercises"][0]["nf_calories"],
    }
}
```

The recorded information includes:

- Date
- Time
- Exercise
- Duration
- Calories

### 5. Send the Data to Sheety

The formatted workout data is sent to the Sheety endpoint using another `POST` request:

```python
response = requests.post(
    url=SHEETY_ENDPOINT,
    json=sheety_params,
    headers=sheet_headers
)
response.raise_for_status()
```

The Sheety API then adds the workout information to the connected spreadsheet.

## API Pipeline

The overall workflow is:

**User input → Exercise API → structured workout data → data transformation → Sheety API → spreadsheet**

This demonstrates how information returned by one external service can be transformed into a request for another external service.

## Authentication

The project demonstrates two different approaches to API authentication.

The exercise API uses custom headers:

```python
exercise_headers = {
    "x-app-id": X_APP_ID,
    "x-app-key": X_APP_KEY
}
```

The Sheety API uses a Bearer token:

```python
sheet_headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}
```

## Error Handling

Both API requests use:

```python
response.raise_for_status()
```

This ensures unsuccessful HTTP responses raise an exception instead of being silently treated as successful requests.

## Concepts Practiced

- REST APIs
- HTTP `POST`
- API authentication
- Request headers
- JSON
- `requests`
- Environment variables
- `python-dotenv`
- Nested dictionaries
- Data extraction
- Data transformation
- `datetime`
- Spreadsheet APIs
- API chaining
- Error handling

## Development Notes

Day 38 builds directly on the API concepts from the previous days.

Instead of simply retrieving information or triggering an email, this project creates a data pipeline between multiple services:

1. Accept natural-language input.
2. Send the input to an external API.
3. Receive structured data.
4. Extract the relevant fields.
5. Transform the data into another API's expected format.
6. Authenticate with the second service.
7. Store the result in a spreadsheet.

## Security Note

API credentials are loaded through environment variables rather than being stored directly in the Python source code.

The `.env` file should remain local and be excluded from version control.

## Course Attribution

The project concepts and exercises originate from **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

## Disclosure

This README was written with AI assistance. **Any code authored by me in this repository was written independently by me.**
