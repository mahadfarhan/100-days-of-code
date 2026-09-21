# Day 48 — Selenium Cookie Clicker Bot

Day 48 of **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu introduced **browser automation with Selenium**.

The main project is a Cookie Clicker bot that controls a browser, continuously clicks the cookie, periodically checks available upgrades, purchases an affordable upgrade, and reports the final cookies-per-second after a five-minute run.

## What I Learned

- Selenium WebDriver
- Browser automation
- Finding HTML elements
- Clicking elements programmatically
- `WebDriverWait`
- Expected conditions
- Waiting for elements to become available
- Handling stale DOM elements
- Reading and parsing webpage text
- Element IDs, classes, CSS selectors, XPath, and other locators
- Continuous automation loops
- Time-based automation with `time.time()`

## Exercises

The exercises introduce Selenium's basic browser-control functionality.

One exercise opens a practice newsletter page, locates form fields by their `name` attributes, enters information, finds the submit button with a CSS selector, and clicks it.

Another exercise explores different element-locating strategies, including:

- `By.ID`
- `By.NAME`
- `By.CLASS_NAME`
- `By.LINK_TEXT`
- `By.CSS_SELECTOR`
- `By.XPATH`
- `By.TAG_NAME`

It also demonstrates retrieving information from elements and iterating through multiple elements on a page.

## Cookie Clicker Bot

The main project launches Chrome with Selenium and opens Cookie Clicker:

```python
def set_up():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://ozh.github.io/cookieclicker/")
    return driver
```

The program selects English using an explicit wait and then waits for the old language element to become stale after the page updates.

```python
eng_lang = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "langSelect-EN"))
)

eng_lang.click()

WebDriverWait(driver, 10).until(
    EC.staleness_of(eng_lang)
)
```

## Reading Upgrade Prices

The bot periodically retrieves upgrade prices using the `price` class:

```python
prices = driver.find_elements(By.CLASS_NAME, "price")
```

Displayed values are cleaned and converted into numbers. The implementation handles prices displayed in:

- millions
- billions
- trillions

For example:

```python
if "million" in parts:
    current_price = float(parts[0]) * 1000000
elif "billion" in parts:
    current_price = float(parts[0]) * 1000000000
elif "trillion" in parts:
    current_price = float(parts[0]) * 1000000000000
```

## Handling Stale Elements

Because the game is constantly updating its DOM, Selenium can encounter `StaleElementReferenceException`.

The price-reading function retries when this occurs:

```python
except StaleElementReferenceException:
    continue
```

This allows the bot to keep operating when the page changes while elements are being read.

## Reading Game Data

The current cookie count and cookies-per-second value are extracted from the game interface and converted from displayed strings into numbers.

For example:

```python
current_cookies = get_cookies(driver)
current_cookies = float(
    current_cookies.split()[0].replace(",", "")
)
```

## Upgrade Selection

The upgrade-selection logic checks the available prices against the current number of cookies:

```python
def check_for_upgrades(prices_list, current_cookies_num):
    for index, price in reversed(list(enumerate(prices_list))):
        if current_cookies_num >= price:
            return index
```

The list is traversed in reverse order so the bot selects the highest-indexed upgrade it can currently afford.

It then locates the corresponding product by ID and clicks it:

```python
upgrade = driver.find_element(
    By.ID,
    value=f"product{upgrade_index}"
)
upgrade.click()
```

## Main Automation Loop

The bot runs for five minutes:

```python
game_duration = 300
timeout_duration = 10
```

The main cookie is clicked continuously. Every ten seconds, the bot:

1. Reads the upgrade prices.
2. Reads the current cookie count.
3. Finds an affordable upgrade.
4. Purchases it if one is available.

At the end of five minutes, it prints the final cookies-per-second value.

```text
Continuous
    ↓
Click cookie

Every 10 seconds
    ↓
Read prices
    ↓
Read cookies
    ↓
Find affordable upgrade
    ↓
Purchase upgrade

After 5 minutes
    ↓
Report final cookies-per-second
```

## Project Structure

```text
Day 48/
├── cookie clicker/
│   └── main.py
│
└── exercises/
    ├── challenge.py
    ├── interaction.py
    └── main.py
```

## Concepts Practiced

### Selenium

- `webdriver.Chrome()`
- `ChromeOptions`
- `driver.get()`
- `find_element()`
- `find_elements()`
- `click()`
- `send_keys()`
- `WebDriverWait`
- Expected conditions
- `presence_of_element_located`
- `staleness_of`

### Python

- Functions
- Lists
- `enumerate()`
- `reversed()`
- String manipulation
- Numeric conversion
- `try` / `except`
- `while` loops
- `time.time()`

### Automation

- Browser control
- DOM interaction
- Reading dynamically changing webpage data
- Handling stale elements
- Periodic task execution
- Decision-making inside an automation loop

## Development Notes

Day 48 represents another significant step in the progression:

**Python → web requests → web scraping → APIs → browser automation**

Earlier projects primarily retrieved and processed information. Selenium allows Python to control an actual browser and interact with a live webpage.

The Cookie Clicker project combines:

**Browser control + DOM interaction + data extraction + decision-making + repeated automation**

The upgrade-selection logic was implemented independently as part of the project solution.

## Course Attribution

The project concepts and exercises originate from **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

## Disclosure

This README was written with AI assistance. **Any code authored by me in this repository was written independently by me.**
