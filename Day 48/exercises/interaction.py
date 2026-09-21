from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# article_count = driver.find_element(By.ID, "mwDw")
# article_count.click()

# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# search_icon = driver.find_element(
#     By.CLASS_NAME,
#     value="mw-ui-icon-wikimedia-search",
# )
# search_icon.click()
# search = driver.find_element(By.NAME, value="search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

driver.get("https://appbrewery.github.io/fake-newsletter-signup/")

f_name = driver.find_element(By.NAME, value="fName")
f_name.send_keys("Mahad")

l_name = driver.find_element(By.NAME, value="lName")
l_name.send_keys("Farhan")

email = driver.find_element(By.NAME, value="email")
email.send_keys("asohduisahd@gmail.com")

sign_up = driver.find_element(
    By.CSS_SELECTOR, value=".btn.btn-lg.btn-primary.btn-block"
)
sign_up.click()

driver.quit()
