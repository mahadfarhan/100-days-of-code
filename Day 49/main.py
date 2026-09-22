from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from dotenv import load_dotenv
import os

load_dotenv()

MY_EMAIL = os.getenv("ACCOUNT_EMAIL")
MY_PASSWORD = os.getenv("ACCOUNT_PASSWORD")


def set_up():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
    chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://appbrewery.github.io/gym/")

    return driver


def login(driver):
    login_btn = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "login-button"))
    )
    login_btn.click()

    email = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "email-input"))
    )
    email.clear()
    email.send_keys(MY_EMAIL)

    password = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "password-input"))
    )
    password.clear()
    password.send_keys(MY_PASSWORD)

    submit_btn = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "submit-button"))
    )
    submit_btn.click()

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "schedule-page"))
    )


def get_booking_date(day):
    booking_date = day.find_element(By.TAG_NAME, value="h2")
    booking_date = booking_date.text.split("(")[-1].replace(")", "")

    return booking_date


def get_booking_info(day_element):
    class_type = day_element.find_element(By.TAG_NAME, value="h3").text
    booking_btn = day_element.find_element(By.TAG_NAME, value="button")
    return class_type, booking_btn


def process_booking(driver, booking_btn, class_type, booking_date):
    outcome = ""
    detail_message = ""
    message_string = ""
    booking_text = booking_btn.text.lower()
    if booking_text == "booked":
        message_string += "Already booked:"
        outcome = "already"
        detail_message += "[Already booked]"
    elif booking_text == "waitlisted":
        message_string += "Already on waitlist:"
        outcome = "already"
        detail_message += "[Already waitlisted]"
    elif "waitlist" in booking_text:
        booking_btn_id = booking_btn.get_attribute("id")
        retry(
            driver,
            click_and_verify_booking,
            7,
            booking_btn_id,
            "Waitlisted",
            description="Booking",
        )
        message_string += "Joined waitlist for:"
        outcome = "waitlisted"
        detail_message += "[New Waitlist]"
    elif "book" in booking_text:
        booking_btn_id = booking_btn.get_attribute("id")
        retry(
            driver,
            click_and_verify_booking,
            7,
            booking_btn_id,
            "Booked",
            description="Booking",
        )
        message_string += "Booked:"
        outcome = "booked"
        detail_message += "[New Booking]"

    final_message = f"{message_string} {class_type} on {booking_date}"
    print(f"✓ {final_message}")
    dynamic_message = f"• {detail_message} {class_type} on {booking_date}"
    return outcome, dynamic_message


def get_class_time(day):
    day_element = day.find_element(
        By.XPATH,
        ".//p[starts-with(@id, 'class-time-') and contains(@id, '1800')]/ancestor::div[contains(@id, 'class-card')][1]",
    )

    return day_element


def get_day(driver):
    sched_page = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "schedule-page"))
    )

    target_days = sched_page.find_elements(
        By.CSS_SELECTOR, "[id^='day-group-'][id*='tue'],[id^='day-group-'][id*='thu']"
    )

    return target_days


def final_counter(final_dict, final_details):
    print(f"""--- BOOKING SUMMARY ---
New bookings: {final_dict['booked']}
New waitlist entries: {final_dict['waitlisted']}
Already booked/waitlisted: {final_dict['already']}
Total Tuesday & Thursday 6pm classes: {final_dict['booked'] + final_dict['waitlisted'] + final_dict['already']}
--- DETAILED CLASS LIST ---
""")

    for detail in final_details:
        print(detail)


def process_day(driver, day):

    day_card = get_class_time(day)
    day_class_type, day_booking_btn = get_booking_info(day_card)
    day_booking_date = get_booking_date(day)
    return process_booking(driver, day_booking_btn, day_class_type, day_booking_date)


def book_first_class(driver):
    target_days = get_day(driver)
    final_dict = {"booked": 0, "waitlisted": 0, "already": 0}
    details_list = []
    for day in target_days:
        outcome, final_message = process_day(driver, day)
        final_dict[outcome] += 1
        details_list.append(final_message)
    final_counter(final_dict, details_list)
    return len(target_days)


def go_to_bookings_page(driver):
    driver.get("https://appbrewery.github.io/gym/my-bookings/")


def get_list_of_bookings(driver, num_of_classes):
    go_to_bookings_page(driver)
    bookings_page = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "my-bookings-page"))
    )
    list_of_bookings = bookings_page.find_elements(
        By.CSS_SELECTOR,
        value="[id='confirmed-bookings-section'] [class*='MyBookings_bookingCard']",
    )
    list_of_waitlists = bookings_page.find_elements(
        By.CSS_SELECTOR,
        value="[id='waitlist-section'] [class*='MyBookings_bookingCard']",
    )

    num_found = len(list_of_bookings) + len(list_of_waitlists)
    if num_found != num_of_classes:
        raise NoSuchElementException

    return list_of_waitlists, list_of_bookings


def get_booking_page_info(driver):
    number_of_classes_booked = book_first_class(driver)
    list_of_waitlists, list_of_bookings = retry(
        driver,
        get_list_of_bookings,
        7,
        number_of_classes_booked,
        description="Bookings retrieval",
    )

    total_number_on_page = len(list_of_waitlists) + len(list_of_bookings)
    print(f"--- Total Tuesday/Thursday 6pm classes: {total_number_on_page} ---")
    print("--- VERIFYING ON MY BOOKINGS PAGE ---")
    for waitlist in list_of_waitlists:
        class_name = waitlist.find_element(By.TAG_NAME, value="h3").text
        print(f"✓ Verified: {class_name}")

    for booking in list_of_bookings:
        class_name = booking.find_element(By.TAG_NAME, value="h3").text
        print(f"✓ Verified: {class_name}")

    print("--- VERIFICATION RESULT ---")
    print(f"Expected: {number_of_classes_booked} bookings")
    print(f"Found: {total_number_on_page} bookings")

    if number_of_classes_booked == total_number_on_page:
        print("✅ SUCCESS: All bookings verified!")
    else:
        print(
            f"❌ MISMATCH: Difference is {number_of_classes_booked - total_number_on_page} bookings"
        )


def click_and_verify_booking(driver, button_id, expected_state):
    current_button = driver.find_element(By.ID, button_id)
    if current_button.text == expected_state:
        return
    else:
        current_button.click()
    WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element((By.ID, button_id), expected_state)
    )


def retry(driver, func, retries, *args, description=None):
    for i in range(retries):
        try:
            return func(driver, *args)
        except (TimeoutException, NoSuchElementException):
            if description is None:
                print(f"{func.__name__} Attempt {i+1} failed")
            else:
                print(f"{description} Attempt {i+1} failed")
            if i == retries - 1:
                raise


driver = set_up()
retry(driver, login, 5, description="Login")
get_booking_page_info(driver)
