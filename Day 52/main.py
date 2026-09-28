from dotenv import load_dotenv
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.action_chains import ActionChains

load_dotenv()

INSTAGRAM_USERNAME = os.getenv("INSTAGRAM_USERNAME")
INSTAGRAM_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")
SIMILAR_ACCOUNT = "chefsteps"
BASE_URL = "https://app.100daysofpython.dev/services/share-a-naan"


class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get(BASE_URL)
        email = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "username"))
        )
        email.send_keys(INSTAGRAM_USERNAME)

        password = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "password"))
        )
        password.send_keys(INSTAGRAM_PASSWORD)

        login_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        login_btn.click()

        dismiss_popup = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "naan-popup-dismiss"))
        )
        dismiss_popup.click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h2[contains(text(), 'Turn on notifications')]")
            )
        )

        dismiss_login_btn = self.driver.find_element(
            By.XPATH, value="//button[contains(text(), 'Not Now')]"
        )
        dismiss_login_btn.click()

    def find_follower(self):
        self.driver.get(f"{BASE_URL}/u/{SIMILAR_ACCOUNT}")
        followers_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div span a"))
        )

        follower_count = int(followers_btn.text.split()[0])

        followers_btn.click()

        self.followers_list = self.driver.find_elements(
            By.CLASS_NAME, value="naan-follower-row"
        )

        while len(self.followers_list) < follower_count:

            naan_scroll = self.driver.find_element(
                By.CLASS_NAME, value="followers-scroll"
            )

            self.driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollHeight", naan_scroll
            )

            self.followers_list = self.driver.find_elements(
                By.CLASS_NAME, value="naan-follower-row"
            )

    def follow(self):
        for follower in self.followers_list:
            follow_button = follower.find_element(By.TAG_NAME, value="button")
            if follow_button.text == "Follow":
                follow_button.click()


instafollower = InstaFollower()
instafollower.login()
instafollower.find_follower()
instafollower.follow()
