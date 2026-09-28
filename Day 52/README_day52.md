# Instagram Follower Automation Bot

A browser-automation project built with Python and Selenium for the Instagram follower challenge. The bot logs into the course's practice Instagram environment, navigates to the followers of a similar account, scrolls through the complete follower list, and follows every account that is not already being followed.

The project combines Selenium browser automation, explicit waits, dynamic scrolling, DOM interaction, environment variables, and class-based organization.

## Features

- Launches Chrome automatically with Selenium
- Loads login credentials from environment variables
- Logs into the course's practice Instagram environment
- Handles post-login popups
- Navigates to a specified similar account
- Retrieves the account's follower count
- Opens the follower list
- Dynamically scrolls through the follower container
- Continues scrolling until all followers have been loaded
- Stores the loaded follower elements
- Checks each follower's current button state
- Follows accounts whose button reads `Follow`
- Skips accounts that are already being followed
- Uses explicit waits for dynamic page elements
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
- Element names
- Element classes
- Element tags
- JavaScript execution

## How It Works

1. The `InstaFollower` class is instantiated and Chrome is launched.
2. The bot navigates to the course's practice Instagram environment.
3. It waits for the username and password fields to become visible.
4. It enters the credentials loaded from environment variables.
5. It waits for and clicks the login button.
6. It dismisses the initial popup.
7. It waits for the notification prompt and clicks `Not Now`.
8. It navigates to the specified similar account.
9. It retrieves the account's follower count.
10. It opens the follower list.
11. It repeatedly scrolls the follower container until the number of loaded follower elements matches the displayed follower count.
12. It iterates through the complete follower list.
13. If a follower's button says `Follow`, the bot clicks it.
14. Accounts that are already followed are left unchanged.

## Login

The login process is handled by `login()`.

Credentials are loaded through environment variables:

```python
load_dotenv()

INSTAGRAM_USERNAME = os.getenv("INSTAGRAM_USERNAME")
INSTAGRAM_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")
```

The bot waits for the login fields before entering the credentials:

```python
email = WebDriverWait(self.driver, 10).until(
    EC.visibility_of_element_located((By.NAME, "username"))
)

email.send_keys(INSTAGRAM_USERNAME)
```

The password field is handled in the same way.

The login button is located with a CSS selector:

```python
login_btn = WebDriverWait(self.driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
)

login_btn.click()
```

## Popup Handling

After logging in, the practice environment presents additional interface elements that need to be dismissed before the follower workflow can continue.

The first popup is located by class name and clicked once it becomes available.

The bot then waits for the notification prompt to appear and dismisses it using its `Not Now` button.

This keeps the login workflow separate from the follower-processing logic.

## Finding the Followers

The target account is defined as:

```python
SIMILAR_ACCOUNT = "chefsteps"
```

The bot navigates directly to that account's page:

```python
self.driver.get(f"{BASE_URL}/u/{SIMILAR_ACCOUNT}")
```

It then locates the followers link and extracts the displayed follower count:

```python
followers_btn = WebDriverWait(self.driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "div span a"))
)

follower_count = int(followers_btn.text.split()[0])
```

After opening the follower list, the currently loaded follower rows are collected:

```python
self.followers_list = self.driver.find_elements(
    By.CLASS_NAME,
    value="naan-follower-row"
)
```

## Dynamic Scrolling

The follower list does not necessarily load every follower immediately.

The bot therefore keeps checking the number of loaded follower rows:

```python
while len(self.followers_list) < follower_count:
```

It locates the scrollable follower container and uses JavaScript to move it to the bottom:

```python
naan_scroll = self.driver.find_element(
    By.CLASS_NAME,
    value="followers-scroll"
)

self.driver.execute_script(
    "arguments[0].scrollTop = arguments[0].scrollHeight",
    naan_scroll
)
```

After each scroll, the follower elements are retrieved again.

This continues until the number of loaded followers reaches the displayed follower count.

## Following Accounts

Once the follower list is complete, the `follow()` method iterates through every follower:

```python
for follower in self.followers_list:
    follow_button = follower.find_element(
        By.TAG_NAME,
        value="button"
    )

    if follow_button.text == "Follow":
        follow_button.click()
```

The button's displayed text determines whether an action is necessary.

- `Follow` → click the button
- Any other state → leave the account unchanged

This prevents the bot from attempting to follow accounts that are already followed.

## Automation Flow

```text
Start Bot
    ↓
Launch Chrome
    ↓
Open practice Instagram
    ↓
Log in
    ↓
Dismiss popup
    ↓
Dismiss notification prompt
    ↓
Open similar account
    ↓
Read follower count
    ↓
Open followers
    ↓
┌──────────────────────────────┐
│ Load follower rows           │
│          ↓                   │
│ Is loaded count < total?     │
│          ↓                   │
│ Scroll follower container    │
│          ↓                   │
│ Reload follower rows         │
│          ↓                   │
│ Repeat until complete        │
└──────────────────────────────┘
    ↓
Iterate through followers
    ↓
Check button state
    ↓
If "Follow" → Click
    ↓
Continue until complete
```

## Project Structure

```text
Day 52/
└── main.py
```

## What I Learned

This project builds on the Selenium concepts from the previous days while introducing dynamic scrolling and a more involved DOM-processing workflow.

Key concepts included:

- Organizing browser automation with a class
- Using `__init__()` to initialize the automation
- Loading credentials with environment variables
- Using explicit waits for dynamic webpage elements
- Locating elements using names, classes, CSS selectors, XPath, and tags
- Reading numeric information from webpage text
- Working with dynamically loaded lists
- Using JavaScript to control a scrollable DOM element
- Re-querying the DOM after page changes
- Iterating through collections of Selenium elements
- Checking an element's current state before interacting with it
- Automating a multi-stage browser workflow

## Development Notes

Day 52 continues the progression of Selenium browser automation into increasingly dynamic webpages.

The progression is:

**Browser control → element interaction → explicit waits → dynamic DOM handling → popup management → scrolling → bulk interaction**

Unlike the earlier projects, the follower list is not fully available immediately. The program has to determine how many followers exist, repeatedly scroll the appropriate container, and re-query the page until the complete list has been loaded.

The complete workflow combines:

**Authentication + popup handling + dynamic scrolling + DOM extraction + state checking + repeated browser interaction**

## Course Attribution

The project concepts and exercises originate from **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

## Disclosure

This README was written with AI assistance. **Any code authored by me in this repository was written independently by me.**

Course-provided instructional material, starter code, project structures, assets, and example implementations are not claimed as my original work.

## Disclaimer

This project was created for educational use with the course's practice environment. It should not be used to automate real services without permission or in violation of their terms of service.
