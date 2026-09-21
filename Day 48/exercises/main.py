from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
# print(f"The price is {price_dollar}.{price_cents}")

# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))

# button = driver.find_element(By.ID, value="submit")
# print(button.size)

# documentation_link = driver.find_element(
#     By.CSS_SELECTOR, value=".documentation-widget a"
# )
# print(documentation_link.text)

# bug_link = driver.find_element(
#     By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a'
# )
# print(bug_link.text)

events_list = driver.find_element(By.CSS_SELECTOR, ".event-widget")
events = events_list.find_elements(By.TAG_NAME, "li")

events_dict = {}

for index, event in enumerate(events):
    date = event.find_element(By.TAG_NAME, "time").text
    name = event.find_element(By.TAG_NAME, "a").text
    events_dict[index] = {"time": date, "name": name}

print(events_dict)

# driver.close()
driver.quit()
