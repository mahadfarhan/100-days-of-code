# Day 37 — Pixela Habit Tracker API

Day 37 of **Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp** focused on working with an external API and learning how to create, update, and delete resources using HTTP requests.

This project uses the **Pixela API** to create and manage a graph for tracking study time.

## What This Day Covers

- Working with REST APIs
- HTTP `POST` requests
- HTTP `PUT` requests
- HTTP `DELETE` requests
- API endpoints
- Request headers
- JSON request bodies
- Environment variables
- `.env` files with `python-dotenv`
- `datetime`
- Dynamic date formatting
- API resource management

## Project Structure

```text
Day 37/
└── main.py
```

The API authentication token is stored in an environment variable and should not be committed to GitHub.

## Pixela Study Tracker

The project uses Pixela to create a graph for tracking the number of hours studied each day.

The graph is configured with:

```python
graph_config = {
    "id": GRAPH_ID,
    "name": "studying",
    "unit": "hours",
    "type": "float",
    "color": "kuro",
}
```

The graph therefore records study time as a floating-point number of hours.

## API Operations

The project demonstrates several different API operations.

### Create a User

A `POST` request can be used to create a Pixela user:

```python
response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
```

This code is currently commented out after the initial setup.

### Create a Graph

A second `POST` request creates the study graph:

```python
response = requests.post(
    url=GRAPH_ENDPOINT,
    json=graph_config,
    headers=headers
)
```

### Add a Daily Pixel

A daily study value is added using another `POST` request:

```python
response = requests.post(
    url=PIXEL_ENDPOINT,
    json=pixel_config,
    headers=headers
)
```

The date is generated dynamically using:

```python
today.strftime("%Y%m%d")
```

The amount of study time is collected from the user:

```python
"quantity": input("How many hours have you studied today?")
```

### Update a Pixel

The project also demonstrates using `PUT` to update an existing day's value:

```python
response = requests.put(
    url=PIXEL_UPDATE_ENDPOINT,
    json=pixel_update_config,
    headers=headers
)
```

The endpoint uses the current date dynamically.

### Delete a Pixel

A `DELETE` request can remove a specific day's pixel:

```python
response = requests.delete(
    url=PIXEL_DELETE_ENDPOINT,
    headers=headers
)
```

This operation is currently commented out.

### Delete the User

The project also includes the endpoint for deleting the entire Pixela user:

```python
DELETE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}"
```

The actual deletion request is intentionally commented out.

## Authentication

The Pixela token is loaded from an environment variable:

```python
TOKEN = os.getenv("AUTH_TOKEN")
```

and supplied through the request header:

```python
headers = {"X-USER-TOKEN": TOKEN}
```

This keeps the authentication token out of the Python source code.

## Date Handling

The project uses Python's `datetime` module to generate the current date:

```python
today = datetime.now()
```

The date is formatted in the form required by the API:

```python
today.strftime("%Y%m%d")
```

This allows the same code to work with the current day without hardcoding a date.

## Concepts Practiced

- REST APIs
- HTTP methods
- `POST`
- `PUT`
- `DELETE`
- Request headers
- JSON request data
- `requests`
- Environment variables
- `python-dotenv`
- `datetime`
- `strftime()`
- User input
- API authentication
- Creating resources
- Updating resources
- Deleting resources

## Development Notes

Day 37 expands on the API concepts introduced in previous days by demonstrating that APIs are not limited to retrieving information.

The project works with the full lifecycle of API resources:

**Create → Read/Use → Update → Delete**

It also demonstrates how authentication information can be supplied through request headers and how dynamically generated dates can be incorporated into API endpoints and request data.

The final code keeps the different API operations visible as commented examples, making the file useful as a reference for the different HTTP methods practiced during the lesson.

## Course Attribution

The project concept, Pixela API exercises, requirements, and learning objectives originate from **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

## Disclosure

This README was written with AI assistance. **The code attribution and implementation details reflect the work completed for the course project.**
