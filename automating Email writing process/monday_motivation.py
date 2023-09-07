import smtplib
import datetime as dt
import random

EMAIL = "your email"
PASSWORD = "your password"
now = dt.datetime.now()
weekday = now.weekday()
if weekday == 5:
    with open("quotes.txt") as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtb.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg=f"subject:MONDAY MOTIVATION\n\n{quote}")
