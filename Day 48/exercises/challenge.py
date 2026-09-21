from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

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
