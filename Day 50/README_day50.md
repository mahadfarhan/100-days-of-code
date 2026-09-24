# Tinder Automation Bot

A browser-automation project built with Python and Selenium for the Tinder challenge. The bot launches a Chrome browser, navigates to the course's Tinder practice environment, logs in through the provided Facebook login flow, handles repeated popups, and automatically likes people.

The project also handles an interaction failure that can occur when a popup intercepts a click, allowing the automation to continue by interacting with the popup before resuming.

## Features

- Launches Chrome automatically with Selenium
- Starts the browser maximized
- Navigates to the course's Tinder practice environment
- Handles the Facebook login flow in a separate browser window
- Switches between browser windows programmatically
- Locates login fields and submits credentials
- Handles repeated popups
- Waits for popup elements to become visible and invisible
- Automatically likes 20 profiles
- Uses explicit waits for dynamic elements
- Handles `ElementClickInterceptedException`
- Detects and interacts with the match popup when it blocks the like button
- Waits for clicked elements to disappear before continuing

## Technologies Used

- Python
- Selenium WebDriver
- ChromeDriver
- Selenium `WebDriverWait`
- Selenium expected conditions
- Browser window management
- Element IDs
- Element classes
- Element tags
- Exception handling

## How It Works

1. Selenium launches Chrome with the browser maximized.
2. The bot navigates to the course's Tinder practice environment.
3. It locates the login button in the page header.
4. It selects the Facebook login option.
5. Selenium waits for the Facebook authentication window to open.
6. The bot switches to the new browser window.
7. It enters the provided username and password and submits the login form.
8. It waits for the authentication window to close.
9. The bot switches back to the original Tinder window.
10. It handles the sequence of popups presented after login.
11. The bot begins liking profiles.
12. After each like, it waits for the like button to become invisible before continuing.
13. If a match popup intercepts a click, the bot waits for the popup's button and interacts with it before continuing.
14. The process repeats until 20 profiles have been liked.

## Facebook Login

The login flow requires Selenium to manage two browser windows.

The bot first waits until two windows are available:

```python
WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
```

It then switches to the second window:

```python
driver.switch_to.window(driver.window_handles[1])
```

The login fields are located by ID and populated before submitting the form.

After authentication, the program waits for the second window to disappear and returns to the original Tinder window.

## Popup Handling

The project contains a dedicated function for dealing with popup cards.

The popup is located by class name, its button by tag name, and explicit waits are used both before and after interaction. The popup handler is called three times after login.

This keeps the popup logic separate from the main liking workflow and prevents the program from continuing before each popup has disappeared.

## Automated Likes

The main automation is handled by `like_people()`.

The function first logs in and then attempts to like 20 profiles.

The like button is located using an explicit wait:

```python
like_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "btn-like"))
)
```

After clicking, the program waits for the button to become invisible:

```python
like_button.click()
WebDriverWait(driver, 10).until(
    EC.invisibility_of_element(like_button)
)
```

This prevents the loop from immediately attempting to reuse an element that is no longer valid after the page changes.

## Handling Interrupted Clicks

A match popup can appear while the bot is attempting to interact with the like button. In that situation, Selenium raises an `ElementClickInterceptedException`.

The project catches this exception and waits for the match popup button to become clickable before interacting with it:

```python
except ElementClickInterceptedException:
    WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "match-popup-link"))
    ).click()
```

Rather than terminating, the bot handles the popup and allows the automation loop to continue.

## Automation Flow

```text
Start Chrome
      ↓
Open Tinder practice environment
      ↓
Click Login
      ↓
Select Facebook Login
      ↓
Wait for second window
      ↓
Switch to Facebook window
      ↓
Enter credentials
      ↓
Submit login
      ↓
Wait for login window to close
      ↓
Return to Tinder
      ↓
Handle 3 popups
      ↓
┌─────────────────────────┐
│ Attempt to like profile │
│          ↓              │
│ Wait for button         │
│          ↓              │
│ Click like              │
│          ↓              │
│ Wait for button to      │
│ become invisible        │
│                         │
│ If match popup blocks   │
│ the click:              │
│ → Handle popup          │
└─────────────────────────┘
      ↓
Repeat 20 times
```

## Project Structure

```text
Day 50/
└── main.py
```

## What I Learned

This project builds on the Selenium concepts introduced in the previous day and adds more complicated browser-state management.

Key concepts included:

- Managing multiple browser windows
- Switching between Selenium window handles
- Automating authentication flows
- Using explicit waits for dynamic UI elements
- Waiting for elements to become visible, clickable, or invisible
- Handling browser interactions interrupted by overlays
- Catching `ElementClickInterceptedException`
- Building reusable popup-handling functions
- Repeating browser interactions reliably
- Using type hints with Selenium's `WebDriver`

## Development Notes

Day 50 continues the progression from basic browser automation toward handling increasingly unpredictable web interfaces.

The progression is:

**Browser control → element interaction → explicit waits → dynamic DOM handling → window management → exception handling → resilient automation**

The project is more complex than simply locating an element and clicking it. The browser can open additional windows, popups can appear unexpectedly, and elements can disappear or become inaccessible during the automation process.

The solution therefore combines:

**Browser control + authentication + window management + explicit waits + popup handling + exception handling + repeated automation**

## Course Attribution

The project concepts and exercises originate from **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

## Disclosure

This README was written with AI assistance. **Any code authored by me in this repository was written independently by me.**

Course-provided instructional material, starter code, project structures, assets, and example implementations are not claimed as my original work.

## Disclaimer

This project was created for educational use with the course's Tinder practice environment. It should not be used to automate real services without permission or in violation of their terms of service.
