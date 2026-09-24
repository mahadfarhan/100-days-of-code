# Internet Speed Twitter Bot

A browser-automation project built with Python and Selenium that checks an internet connection's download and upload speeds and automatically posts a complaint when either speed falls below the promised service speed.

The project combines Selenium browser automation, explicit waits, environment variables, and conditional logic to automate the process from speed testing through posting the complaint.

## Features

- Launches Chrome automatically with Selenium
- Runs an internet speed test through Speedtest
- Waits for download and upload speed results
- Extracts dynamically displayed speed values
- Compares actual speeds against promised speeds
- Loads login credentials from environment variables
- Logs into the course's practice social-media environment when speeds are below the promised values
- Automatically composes a complaint using the measured speeds
- Posts the complaint automatically
- Uses explicit waits for dynamic webpage elements
- Organizes the workflow with a dedicated class

## Technologies Used

- Python
- Selenium WebDriver
- ChromeDriver
- `python-dotenv`
- `os`
- `WebDriverWait`
- Selenium expected conditions
- CSS selectors
- XPath
- Element IDs
- Element classes
- Element tags

## How It Works

1. The `InternetSpeedTwitterBot` class is instantiated.
2. Chrome is launched with Selenium.
3. The bot navigates to Speedtest.
4. It waits for the speed-test button to become clickable and starts the test.
5. It waits for the download and upload speed values to become available.
6. The measured speeds are stored in the object.
7. The values are compared against the promised speeds.
8. If either speed is below the promised value, the bot opens the course's practice social-media environment.
9. It logs in using credentials loaded from environment variables.
10. It writes a complaint containing the measured and promised speeds.
11. It submits the post.

If both measured speeds meet or exceed the promised values, no complaint is posted.

## Speed Test

The speed test is handled by `get_internet_speed()`.

The bot waits for the start button using an explicit wait and CSS selector:

```python
speed_test_btn = WebDriverWait(self.driver, 10).until(
    EC.element_to_be_clickable(
        (
            By.CSS_SELECTOR,
            "button[aria-label='start speed test - connection type multi']",
        )
    )
)
```

After starting the test, it locates the download-speed display and then navigates through the DOM to the element containing the actual speed value.

The bot waits until the display contains a real value rather than the placeholder `—` or an empty string:

```python
WebDriverWait(self.driver, 150).until(
    lambda d: "—" != down_speed.text and "" != down_speed.text
)
```

The upload speed is retrieved using the same approach, using the `Sending Time` element.

The resulting values are stored as instance attributes:

```python
self.down = down_speed.text
self.up = up_speed.text
```

## Speed Comparison

The promised speeds are defined as constants:

```python
PROMISED_DOWN = 150
PROMISED_UP = 150
```

The bot checks whether either measured value falls below its corresponding target:

```python
if float(self.down) < PROMISED_DOWN or float(self.up) < PROMISED_UP:
```

Only when this condition is true does the bot proceed to the complaint workflow.

## Automated Complaint

When the measured connection is below the promised speed, the bot navigates to the course's practice social-media service.

Credentials are loaded through environment variables:

```python
load_dotenv()

TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")
```

The bot waits for the login fields before entering the credentials.

After logging in, it waits for the post-composition field and creates a message containing the measured and promised speeds:

```python
post_text.send_keys(
    f"Hey Internet Provider, why is my internet speed "
    f"{self.down}down/{self.up}up when I pay for "
    f"{PROMISED_DOWN}down/{PROMISED_UP}up"
)
```

It then locates the post button and submits the complaint.

## Automation Flow

```text
Start Bot
    ↓
Launch Chrome
    ↓
Open Speedtest
    ↓
Start Speed Test
    ↓
Wait for Download Speed
    ↓
Wait for Upload Speed
    ↓
Store Results
    ↓
Compare Against Promised Speeds
    ↓
 ┌─────────────────────────────┐
 │ Both speeds meet/exceed     │
 │ promised speeds?             │
 └──────────────┬──────────────┘
                │
        Yes ────┴──── No
        ↓             ↓
   Do nothing     Open practice
                  social-media site
                       ↓
                  Log in
                       ↓
                  Compose complaint
                       ↓
                  Submit post
```

## Project Structure

```text
Day 51/
└── main.py
```

## What I Learned

This project builds on the Selenium browser-automation concepts from previous projects while introducing a more complete automated workflow.

Key concepts included:

- Organizing an automation project with a class
- Using `__init__()` to control program flow
- Storing state in instance attributes
- Extracting dynamically changing values from a webpage
- Using explicit waits for asynchronous webpage behavior
- Using lambda functions as custom wait conditions
- Navigating through the DOM with XPath
- Combining different Selenium locator strategies
- Loading credentials from environment variables
- Comparing scraped values against predefined targets
- Triggering browser actions conditionally
- Automating an end-to-end workflow

## Development Notes

Day 51 expands browser automation beyond interacting with a single webpage.

The progression is:

**Browser automation → dynamic data extraction → conditional logic → authentication → automated action**

The bot gathers information from one website, interprets that information, and then conditionally interacts with a second website.

The complete workflow is:

**Speedtest → scrape results → compare against target → log in → compose complaint → post**

This makes the project an example of an end-to-end automation pipeline rather than a collection of isolated Selenium interactions.

## Course Attribution

The project concepts and exercises originate from **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

## Disclosure

This README was written with AI assistance. **Any code authored by me in this repository was written independently by me.**

Course-provided instructional material, starter code, project structures, assets, and example implementations are not claimed as my original work.

## Disclaimer

This project was created for educational use with the course's practice environment. It should not be used to automate real services without permission or in violation of their terms of service.
