import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
response.raise_for_status()

empire_webpage = response.text

soup = BeautifulSoup(empire_webpage, "html.parser")
articles_desc = soup.select(".article-title-description__text")
articles_list = [article.find("h3").getText() for article in articles_desc]

articles_list.reverse()

with open(
    "./Starting Code - 100 movies to watch start/movies.txt", "w", encoding="utf-8"
) as file:
    for article in articles_list:
        file.write(f"{article}\n")
