# Day 45 — Web Scraping with BeautifulSoup

Day 45 of **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu focused on **web scraping with BeautifulSoup**.

This day was especially relevant to me because web scraping was one of the original reasons I started learning Python.

## What I Learned

- Sending HTTP requests with `requests`
- Parsing HTML with BeautifulSoup
- Selecting HTML elements
- Using CSS selectors
- Extracting text and attributes from HTML
- Working with scraped data in Python
- Finding and indexing values in lists
- Writing scraped results to a text file
- Scraping information from a live website

---

## Exercises

### BeautifulSoup HTML Parsing

The first exercise introduced BeautifulSoup using a local HTML file.

I practiced:

- Reading HTML from a file
- Creating a `BeautifulSoup` object
- Inspecting HTML elements
- Using `.find()` and `.find_all()`
- Using `.getText()` and `.get()`
- Selecting elements with CSS selectors
- Using `soup.select()` and `soup.select_one()`

The exercise provided a small HTML webpage and used it to demonstrate how BeautifulSoup can navigate and extract information from structured HTML.

### Hacker News Scraper

The Hacker News exercise applied the same concepts to a live webpage.

The program:

1. Sends a request to Hacker News using `requests`.
2. Parses the response with BeautifulSoup.
3. Extracts article titles.
4. Extracts article links.
5. Extracts article upvote counts.
6. Converts the upvote counts to integers.
7. Finds the highest number of upvotes.
8. Uses the corresponding index to retrieve the article title and link.

This was a useful step from simply learning how to parse HTML toward actually extracting meaningful information from a website.

---

# 100 Movies That You Must Watch

The main project for Day 45 was **100 Movies That You Must Watch**.

## Objective

The course project asks you to scrape the top 100 movies of all time from a website and generate a text file called `movies.txt` containing the movie titles in ascending order.

The intended output follows this format:

```text
1) The Godfather
2) The Empire Strikes Back
3) The Dark Knight
4) The Shawshank Redemption
...
```

The central purpose of the project is to use BeautifulSoup to obtain data such as movie titles from a curated movie ranking.

## Internet Archive

The course instructions specify using a particular archived version of the Empire movie ranking through the Internet Archive's Wayback Machine.

This keeps the webpage consistent with the course material and ensures that the HTML being scraped matches the version used in the walkthrough.

---

## My Implementation

For the project, I used `requests` to retrieve the archived webpage and BeautifulSoup to parse it:

```python
response = requests.get(URL)
response.raise_for_status()

empire_webpage = response.text

soup = BeautifulSoup(empire_webpage, "html.parser")
```

I then selected the relevant movie entries using a CSS selector:

```python
articles_desc = soup.select(".article-title-description__text")
```

The movie titles were extracted from the `<h3>` elements:

```python
articles_list = [article.find("h3").getText() for article in articles_desc]
```

Because the scraped results appeared in reverse order, I reversed the list:

```python
articles_list.reverse()
```

Finally, I wrote the movie titles to `movies.txt`:

```python
with open(
    "./Starting Code - 100 movies to watch start/movies.txt",
    "w",
    encoding="utf-8"
) as file:
    for article in articles_list:
        file.write(f"{article}\n")
```

The resulting file contains the scraped movie ranking in ascending order.

## Project Structure

```text
Day 45/
├── exercises/
│   ├── live_website/
│   │   └── main.py
│   ├── main.py
│   └── website.html
│
└── Starting Code - 100 movies to watch start/
    ├── main.py
    └── movies.txt
```

## Concepts Practiced

### Python

- List comprehensions
- List indexing
- `max()`
- `.reverse()`
- File I/O
- String formatting

### Requests

- `requests.get()`
- HTTP response handling
- `response.raise_for_status()`
- `response.text`

### BeautifulSoup

- `BeautifulSoup()`
- `.find()`
- `.find_all()`
- `.select()`
- `.select_one()`
- `.getText()`
- `.get()`
- CSS selectors
- Navigating HTML structure

---

## What This Day Represents

Day 45 was a significant point in my Python learning because it brought together several concepts into something much closer to the kind of work I originally wanted to use Python for.

The progression was essentially:

**Python → HTTP requests → HTML → BeautifulSoup → CSS selectors → scraped data → useful output**

The exercises started with parsing a local HTML document, progressed to extracting information from Hacker News, and culminated in scraping a movie ranking and saving the results to a file.

---

## Course Attribution

The project concepts and exercises originate from **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

The original project instructions and course-provided resources are included separately with the project.

## Disclosure

This README was written with AI assistance. **Any code authored by me in this repository was written independently by me.**
