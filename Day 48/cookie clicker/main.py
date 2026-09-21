import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException


def set_up():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://ozh.github.io/cookieclicker/")
    return driver


driver = set_up()


def select_lang(driver):
    eng_lang = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "langSelect-EN"))
    )
    eng_lang.click()
    WebDriverWait(driver, 10).until(EC.staleness_of(eng_lang))


select_lang(driver)


def get_prices(driver):
    while True:
        try:
            prices = driver.find_elements(By.CLASS_NAME, "price")
            prices_text = []
            for price in prices:
                price_text = price.text
                if price_text != "":
                    current_price = price_text.replace(",", "")
                    parts = current_price.split()
                    if "million" in parts:
                        current_price = float(parts[0]) * 1000000
                    elif "billion" in parts:
                        current_price = float(parts[0]) * 1000000000
                    elif "trillion" in parts:
                        current_price = float(parts[0]) * 1000000000000
                    prices_text.append(float(current_price))
            return prices_text

        except StaleElementReferenceException:
            continue


def get_cookies(driver):
    try:
        current_cookies = driver.find_element(By.ID, value="cookies").text
    except StaleElementReferenceException:
        current_cookies = driver.find_element(By.ID, value="cookies").text
    return current_cookies


def get_current_cookies(driver):
    current_cookies = get_cookies(driver)
    current_cookies = float(current_cookies.split()[0].replace(",", ""))
    return current_cookies


def get_cookies_per_second(driver):
    current_cookies_per_sec = get_cookies(driver)
    current_cookies_per_sec = float(
        current_cookies_per_sec.split()[-1].replace(",", "")
    )
    return current_cookies_per_sec


def check_for_upgrades(prices_list, current_cookies_num):
    for index, price in reversed(list(enumerate(prices_list))):
        if current_cookies_num >= price:
            return index


def buy_upgrade(driver, prices_list, current_cookies_num):
    upgrade_index = check_for_upgrades(prices_list, current_cookies_num)
    if upgrade_index is not None:
        upgrade = driver.find_element(By.ID, value=f"product{upgrade_index}")
        upgrade.click()


cookie = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "bigCookie"))
)

game_duration = 300
timeout_duration = 10
game_reset_time = time.time()
upgrade_check_time = time.time()

while True:
    if time.time() - game_reset_time > game_duration:
        print(f"Final cookies per sec: {get_cookies_per_second(driver)}")
        break
    if time.time() - upgrade_check_time > timeout_duration:
        prices_list = get_prices(driver)
        current_cookies_num = get_current_cookies(driver)
        buy_upgrade(driver, prices_list, current_cookies_num)
        upgrade_check_time = time.time()
    cookie.click()
