from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException

import os
from dotenv import load_dotenv

load_dotenv()

PROMISED_DOWN = 150
PROMISED_UP = 150
TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")


class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = 0
        self.up = 0
        self.get_internet_speed()
        self.tweet_at_provider()

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        speed_test_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    "button[aria-label='start speed test - connection type multi']",
                )
            )
        )
        speed_test_btn.click()

        down_child_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "svg[aria-label='Receiving Time']")
            )
        )

        down_div = down_child_element.find_element(By.XPATH, "./ancestor::div[1]")
        down_speed = down_div.find_element(By.TAG_NAME, value="h3")
        WebDriverWait(self.driver, 150).until(
            lambda d: "—" != down_speed.text and "" != down_speed.text
        )

        up_child_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "svg[aria-label='Sending Time']")
            )
        )

        up_div = up_child_element.find_element(By.XPATH, "./ancestor::div[1]")
        up_speed = up_div.find_element(By.TAG_NAME, value="h3")
        WebDriverWait(self.driver, 150).until(
            lambda d: "—" != up_speed.text and "" != up_speed.text
        )
        self.down = down_speed.text
        self.up = up_speed.text

    def tweet_at_provider(self):

        if float(self.down) < PROMISED_DOWN or float(self.up) < PROMISED_UP:
            self.driver.get("https://app.100daysofpython.dev/services/y")
            login_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "y-login-link"))
            )
            login_btn.click()

            email = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "email"))
            )
            email.send_keys(TWITTER_EMAIL)

            password = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "password"))
            )
            password.send_keys(TWITTER_PASSWORD)

            login_btn = self.driver.find_element(By.TAG_NAME, value="button")
            login_btn.click()

            post_text = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, "div[aria-label='Post text']")
                )
            )

            post_text.send_keys(
                f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up"
            )

            post_btn = self.driver.find_element(By.ID, value="post-btn")
            post_btn.click()


internetspeedtwitterbot = InternetSpeedTwitterBot()
