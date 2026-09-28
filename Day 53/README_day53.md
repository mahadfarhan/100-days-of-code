# Zillow Rental Data Automation

A web-scraping and browser-automation project built with Python, BeautifulSoup, and Selenium. The program scrapes rental listing information from a Zillow-style practice website, extracts addresses, prices, and listing links, and automatically submits that information through a Google Form.

The project combines HTTP requests, HTML parsing, regular expressions, data collection, and Selenium browser automation into a single end-to-end workflow.

## Features

- Requests webpage data with `requests`
- Parses HTML with BeautifulSoup
- Extracts rental listing information from multiple listings
- Collects listing addresses, prices, and links into separate lists
- Cleans scraped address text
- Cleans price strings with regular expressions
- Launches Chrome automatically with Selenium
- Opens a Google Form
- Dynamically locates form fields
- Enters each rental listing into the form
- Submits each response automatically
- Returns to the form to submit the next listing
- Uses explicit waits for dynamic webpage elements

## Technologies Used

- Python
- `requests`
- BeautifulSoup
- `re`
- Selenium WebDriver
- ChromeDriver
- `WebDriverWait`
- Selenium expected conditions
- CSS selectors
- Tag-name selectors

## How It Works

1. The program requests the Zillow-style practice webpage.
2. It checks that the request was successful.
3. BeautifulSoup parses the returned HTML.
4. The program selects all rental listing containers.
5. For each listing, it extracts the listing URL, price, and address.
6. The scraped values are cleaned and stored in separate lists.
7. Selenium launches Chrome and opens the Google Form.
8. For every scraped listing, the bot waits for the form's text fields to become available.
9. It enters the address, price, and listing link into the corresponding fields.
10. It submits the form.
11. It clicks the link to submit another response.
12. The process repeats until every scraped listing has been entered.

## Scraping the Listings

The program requests the practice Zillow page:

```python
URL = "https://appbrewery.github.io/Zillow-Clone/"
response = requests.get(URL)
response.raise_for_status()
```

The returned HTML is passed to BeautifulSoup:

```python
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
listings = soup.select(".StyledPropertyCardDataWrapper")
```

The program loops through every listing and extracts the relevant information:

```python
for listing in listings:
    link_of_listing = listing.find("a").get("href")
    price_of_listing = listing.find("span").text.split()[0]
    address_of_listing = listing.find("address").text.strip().replace("|", "")
```

The three values are stored separately:

```python
links.append(link_of_listing)
prices.append(price_of_listing)
addresses.append(address_of_listing)
```

Keeping the values in corresponding lists allows each address, price, and link to be submitted together later.

## Data Cleaning

The scraped price is cleaned with a regular expression:

```python
price_of_listing = re.sub(r"[^0-9$,]", "", price_of_listing)
```

The address is normalized by removing the separator character and collapsing repeated whitespace:

```python
address_of_listing = address_of_listing.strip().replace("|", "")
address_of_listing = re.sub(r"\s+", " ", address_of_listing)
```

This produces cleaner values before they are entered into the form.

## Google Form Automation

After collecting the listing information, Selenium opens the Google Form:

```python
driver.get(
    "https://docs.google.com/forms/d/e/1FAIpQLSdhYQfkV8iC8bfOvYgS34ru-nVCTBDTb_1zWzwKdhcAlx1Eww/viewform?usp=publish-editor"
)
```

For each listing, the program waits for the text inputs to become clickable and retrieves the available fields:

```python
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='text']"))
)

list_of_answers = driver.find_elements(
    By.CSS_SELECTOR,
    "input[type='text']"
)
```

The corresponding listing information is entered into the three fields:

```python
list_of_answers[0].send_keys(addresses[i])
list_of_answers[1].send_keys(prices[i])
list_of_answers[2].send_keys(links[i])
```

## Form Submission

The submit button is located using its ARIA role:

```python
submit_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "div[role='button']"))
)

submit_btn.click()
```

After submission, the bot waits for the option to submit another response:

```python
submit_another_response = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.TAG_NAME, "a"))
)

submit_another_response.click()
```

This allows the same browser session to process every rental listing automatically.

## Automation Flow

```text
Request Zillow practice webpage
          ↓
Parse HTML with BeautifulSoup
          ↓
Find all rental listings
          ↓
┌─────────────────────────────┐
│ Extract address             │
│ Extract price               │
│ Extract listing URL         │
│ Clean scraped values        │
└─────────────────────────────┘
          ↓
Store listing data
          ↓
Launch Chrome
          ↓
Open Google Form
          ↓
┌─────────────────────────────┐
│ Enter address               │
│ Enter price                 │
│ Enter listing URL           │
│ Submit form                 │
│ Submit another response     │
└─────────────────────────────┘
          ↓
Repeat for every listing
```

## Project Structure

```text
Day 53/
└── main.py
```

## What I Learned

This project combines two areas of automation that had previously been practiced separately: **web scraping and browser automation**.

Key concepts included:

- Making HTTP requests with `requests`
- Checking HTTP responses with `raise_for_status()`
- Parsing HTML with BeautifulSoup
- Selecting multiple elements with CSS selectors
- Extracting attributes from HTML elements
- Cleaning scraped strings
- Using regular expressions with `re.sub()`
- Maintaining related data in separate lists
- Launching and controlling Chrome with Selenium
- Using explicit waits
- Finding multiple form elements
- Entering scraped data into browser forms
- Automating repeated form submissions
- Combining `requests`, BeautifulSoup, and Selenium in one workflow

## Development Notes

Day 53 brings together several concepts from earlier projects.

The progression is:

**Web requests → web scraping → data cleaning → browser automation → automated form submission**

Instead of simply scraping information and displaying it, the program takes the scraped data and uses it as input for another automated process.

The complete workflow is:

**Scrape listings → clean data → store data → open form → submit listings automatically**

This makes the project an example of an end-to-end data collection and browser-automation pipeline.

## Course Attribution

The project concepts and exercises originate from **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

## Disclosure

This README was written with AI assistance. **Any code authored by me in this repository was written independently by me.**

Course-provided instructional material, starter code, project structures, assets, and example implementations are not claimed as my original work.

## Disclaimer

This project was created for educational use with the course's practice environment. It should not be used to scrape or automate real services without permission or in violation of their terms of service.
