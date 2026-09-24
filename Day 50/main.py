from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException


def set_up():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=chrome_options)

    driver.get(
        "https://app.100daysofpython.dev/services/tindog/u/4ORYyysPdAvmPfpigaehHAKhCPReXHqE"
    )

    return driver


def login_facebook(driver: WebDriver):
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

    driver.switch_to.window(driver.window_handles[1])

    email = driver.find_element(By.ID, value="email")
    email.send_keys("my_username@test.com")

    password = driver.find_element(By.ID, value="pass")
    password.send_keys("password@123")

    submit_btn = driver.find_element(By.TAG_NAME, value="button")
    submit_btn.click()


def deal_with_popup(driver: WebDriver):
    element_popup = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "popup-card"))
    )
    element_btn = element_popup.find_element(By.TAG_NAME, value="button")
    element_btn.click()

    WebDriverWait(driver, 10).until(EC.invisibility_of_element(element_popup))


def popups(driver: WebDriver):
    for _ in range(3):
        deal_with_popup(driver)


def log_in(driver: WebDriver):
    header = driver.find_element(By.TAG_NAME, value="header")
    login_btn = header.find_element(By.TAG_NAME, value="button")
    login_btn.click()

    facebook_login = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "btn-facebark"))
    )
    facebook_login.click()

    current_window = driver.current_window_handle

    login_facebook(driver)

    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(1))

    driver.switch_to.window(current_window)

    popups(driver)


def like_people(driver: WebDriver):
    log_in(driver)
    for _ in range(20):
        try:
            like_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "btn-like"))
            )
            like_button.click()
            WebDriverWait(driver, 10).until(EC.invisibility_of_element(like_button))
        except ElementClickInterceptedException:
            WebDriverWait(driver, 2).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "match-popup-link"))
            ).click()


driver = set_up()
like_people(driver)
