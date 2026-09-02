# Day 32 — Automated Email Sending with SMTP

Day 32 of **Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp** focused on sending automated emails from Python using `smtplib`, combined with file handling, environment variables, and scheduled/conditional logic.

This day includes two separate projects: a **Birthday Wisher** application and a **Monday Motivation** exercise script.

## Project Structure

```text
Day 32/
├── birthday wisher/
│   ├── letter_templates/
│   │   ├── letter_1.txt
│   │   ├── letter_2.txt
│   │   └── letter_3.txt
│   ├── birthdays.csv
│   └── main.py
├── exercises/
│   ├── main.py
│   └── quotes.txt
├── .env
└── .gitignore
```

`.env` stores email credentials and recipient addresses locally and is excluded from version control via the root `.gitignore`.

A separate, Day-32-scoped `.gitignore` was also added to exclude `birthdays.csv`, since that file contains real names and email addresses rather than placeholder data.

## What This Day Covers

- Sending emails programmatically with `smtplib`
- Securing SMTP connections with `starttls()`
- Managing credentials safely using environment variables (`python-dotenv`)
- Reading and writing CSV data with Pandas
- Reading and processing text files
- Randomized template/content selection
- Date-based conditional logic (`datetime`)
- Working with multiple related scripts in one day's folder

---

## Project 1: Birthday Wisher

A script that checks a CSV of birthdays and automatically emails a randomly chosen birthday message to anyone whose birthday matches today's date.

### Features

- Reads a list of names, emails, and birthdays from `birthdays.csv`
- Compares each entry's month and day against today's date
- Randomly selects one of three letter templates for variety
- Replaces a `[NAME]` placeholder in the template with the recipient's name
- Sends the personalized message via Gmail's SMTP server

### How It Works

1. `birthdays.csv` is loaded into a Pandas DataFrame.
2. The current day and month are compared against each row to find today's birthdays.
3. For each match, a random letter template is chosen from `letter_templates/`.
4. The `[NAME]` placeholder inside the template is replaced with the actual name.
5. The finished message is emailed to the corresponding address using `smtplib`.

### Example Template (`letter_templates/letter_1.txt`)

```text
Dear [NAME],

Happy birthday!

All the best for the year!

Angela
```

---

## Project 2: Monday Motivation (Exercise)

A smaller companion script that checks whether the current day is a Monday, and if so, emails a randomly selected motivational quote from `quotes.txt`.

### Features

- Checks the current weekday using `datetime.now().weekday()`
- Only sends an email if the day is Monday (`weekday() == 0`)
- Selects a random quote from a large collection in `quotes.txt`
- Sends the quote by email using the same SMTP setup as the Birthday Wisher

### How It Works

1. `quotes.txt` is read and split into a list of individual quotes.
2. The script checks if today is Monday.
3. If it is, a random quote is chosen and emailed to the configured recipient with the subject "Monday Motivation!".

---

## Environment Variables

Both scripts rely on a `.env` file (not committed to the repository) containing:

```text
MY_EMAIL=your_email@example.com
EMAIL_PASSWORD=your_app_password
SEND_TO=recipient_email@example.com
```

Keeping credentials and personal email addresses out of the source code and loading them via `python-dotenv` was a deliberate fix made during development, after an earlier version of the Monday Motivation script had a personal email address hardcoded directly into `main.py`.

## Concepts Practiced

- `smtplib` and SMTP connections
- `starttls()` for secure email transport
- Environment variables and `python-dotenv`
- Pandas DataFrames and CSV filtering
- File reading and string manipulation
- `random.choice()`
- `datetime` for date and weekday logic
- Separating credentials from source code

## Development Notes

Beyond the base project requirements, a few refinements were made independently:

- Moving all sensitive values (email, password, recipient) into environment variables rather than hardcoding them
- Correcting a mismatched email subject line in the Monday Motivation script so it accurately reflects the script's purpose
- Structuring the day's folder to clearly separate the main project (Birthday Wisher) from the supplementary exercise (Monday Motivation)
- Adding a folder-level `.gitignore` to exclude `birthdays.csv`, since it contains real names and email addresses rather than placeholder data

## Course Attribution

The project specifications, learning objectives, and starter datasets (`birthdays.csv`, `quotes.txt`, letter templates) originate from **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

## Disclosure

This README was written with AI assistance.

**All code in this repository was written independently by me.**
