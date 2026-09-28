import requests
from bs4 import BeautifulSoup
import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://appbrewery.github.io/Zillow-Clone/"
response = requests.get(URL)
response.raise_for_status()

webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
listings = soup.select(".StyledPropertyCardDataWrapper")

addresses = []
links = []
prices = []

for listing in listings:
    link_of_listing = listing.find("a").get("href")
    price_of_listing = listing.find("span").text.split()[0]
    price_of_listing = re.sub(r"[^0-9$,]", "", price_of_listing)
    address_of_listing = listing.find("address").text.strip().replace("|", "")
    address_of_listing = re.sub(r"\s+", " ", address_of_listing)
    links.append(link_of_listing)
    prices.append(price_of_listing)
    addresses.append(address_of_listing)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get(
    "https://docs.google.com/forms/d/e/1FAIpQLSdhYQfkV8iC8bfOvYgS34ru-nVCTBDTb_1zWzwKdhcAlx1Eww/viewform?usp=publish-editor"
)

for i in range(len(addresses)):

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='text']"))
    )

    list_of_answers = driver.find_elements(By.CSS_SELECTOR, "input[type='text']")

    list_of_answers[0].send_keys(addresses[i])
    list_of_answers[1].send_keys(prices[i])
    list_of_answers[2].send_keys(links[i])

    submit_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div[role='button']"))
    )
    submit_btn.click()

    submit_another_response = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.TAG_NAME, "a"))
    )
    submit_another_response.click()
