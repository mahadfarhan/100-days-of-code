from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
response.raise_for_status()

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

titlelines = soup.select(".titleline")
article_texts = []
article_links = []
for titleline in titlelines:
    article = titleline.find("a")
    article_texts.append(article.getText())
    article_links.append(article.get("href"))

article_upvotes = soup.select(".score")
article_upvotes_list = [int(upvote.getText().split()[0]) for upvote in article_upvotes]

highest = max(article_upvotes_list)
print(highest)
highest_index = article_upvotes_list.index(highest)

print(f"Title of article with highest upvotes: {article_texts[highest_index]}")
print(f"Link of article with highest upvotes: {article_links[highest_index]}")
print(
    f"Number of upvotes of article with highest upvotes: {article_upvotes_list[highest_index]}"
)
