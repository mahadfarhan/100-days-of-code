# Selenium Gym Booking Bot

A resilient browser-automation project built with Python and Selenium for the Snack & Lift Gym challenge. The bot logs into the gym website, finds every Tuesday and Thursday class scheduled for 6:00 PM, books available classes or joins their waitlists, and verifies the results on the **My Bookings** page.

The project also handles simulated network failures with reusable retry logic, allowing failed login, booking, and booking-retrieval operations to be attempted again safely.

## Features

- Uses a persistent Chrome profile to retain browser preferences
- Loads account credentials securely from environment variables
- Logs into the gym website automatically
- Locates all Tuesday and Thursday day groups dynamically
- Selects only classes scheduled for 6:00 PM
- Books available classes
- Joins waitlists when classes are full
- Recognizes classes that are already booked or waitlisted
- Tracks new bookings, new waitlist entries, and existing reservations
- Prints a detailed booking summary
- Opens the **My Bookings** page and verifies the expected reservations
- Retries failed operations caused by simulated network errors
- Re-locates booking buttons by their unique IDs to avoid relying on outdated elements

## Technologies Used

- Python
- Selenium WebDriver
- ChromeDriver
- `python-dotenv`
- CSS selectors and XPath
- Explicit waits and Selenium expected conditions

## How It Works

1. Selenium starts Chrome using a dedicated local profile.
2. The bot logs in with credentials loaded from a `.env` file.
3. It waits for the class schedule to confirm that login succeeded.
4. It collects all Tuesday and Thursday schedule containers.
5. Within each target day, it locates the class card whose time identifier contains `1800`.
6. It checks the booking button's current state:
   - **Book Class** — books the class.
   - **Join Waitlist** — joins the waitlist.
   - **Booked** — records that the class was already booked.
   - **Waitlisted** — records that the user was already on the waitlist.
7. It prints a summary and detailed list of all processed classes.
8. It navigates to **My Bookings** and compares the reservations found there with the number expected.

## Network Resilience

The site can simulate unreliable network requests. To handle this, the project includes a general-purpose retry wrapper that accepts another function, its arguments, a retry limit, and an optional description.

The retry system is used for:

- Logging in
- Clicking and verifying booking buttons
- Retrieving reservations from the My Bookings page

A booking attempt is considered successful only after the button text changes to the expected state. Before retrying a click, the bot checks whether the previous attempt already succeeded. This prevents an operation from being repeated unnecessarily.

If the My Bookings page returns fewer or more reservations than expected, the retrieval function raises an exception so the operation can be attempted again.

The bot was tested against the site's **50% network failure simulation**, including a run where a booking failed six consecutive times before succeeding on the seventh and final attempt.

## Setup

1. Install Python and Google Chrome.
2. Install the required packages:

   ```bash
   pip install selenium python-dotenv
   ```

3. Create a `.env` file in the project directory:

   ```env
   ACCOUNT_EMAIL=your_email@example.com
   ACCOUNT_PASSWORD=your_password
   ```

4. Make sure `.env` and the generated `chrome_profile` directory are excluded from version control.

5. Run the project:

   ```bash
   python main.py
   ```

## Example Output

```text
Login Attempt 1 failed
Login Attempt 2 failed
✓ Booked: Spin Class on Thu, Sep 24
Booking Attempt 1 failed
✓ Booked: Spin Class on Tue, Sep 29

--- BOOKING SUMMARY ---
New bookings: 2
New waitlist entries: 0
Already booked/waitlisted: 0
Total Tuesday & Thursday 6pm classes: 2

--- VERIFYING ON MY BOOKINGS PAGE ---
✓ Verified: Spin Class
✓ Verified: Spin Class

--- VERIFICATION RESULT ---
Expected: 2 bookings
Found: 2 bookings
✅ SUCCESS: All bookings verified!
```

## Project Structure

```text
.
├── main.py
├── .env
├── .gitignore
└── chrome_profile/
```

The `.env` file and `chrome_profile/` directory should remain private and should not be committed.

## What I Learned

This project began as a straightforward Selenium exercise and developed into an introduction to resilient automation. Key concepts included:

- Breaking a large workflow into focused helper functions
- Passing functions and arguments into a reusable wrapper
- Using explicit waits instead of fixed delays
- Raising and catching exceptions intentionally
- Designing retryable actions to be safe when repeated
- Verifying state changes instead of assuming a click succeeded
- Re-locating dynamic DOM elements after page updates
- Returning values through wrapper functions
- Comparing expected application state with actual persisted state

## Course Attribution

The project concepts and exercises originate from **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

## Disclosure

This README was written with AI assistance. **Any code authored by me in this repository was written independently by me.**

Course-provided instructional material, starter code, project structures, assets, and example implementations are not claimed as my original work.

## Disclaimer

This project was created for educational use with the Snack & Lift Gym practice website. It should not be used to automate real services without permission or in violation of their terms of service.
