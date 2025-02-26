import smtplib
import datetime as dt
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

MY_EMAIL = "testingashan@gmail.com"
MY_PASSWORD = "ashan24019vimodh"  # Replace with App Password if 2FA is on!

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 2:  # Tuesday (0 = Monday, ..., 6 = Sunday)
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes).strip()  # Remove newline characters

    # Create a properly formatted email
    message = MIMEMultipart()
    message["From"] = MY_EMAIL
    message["To"] = "fernando.harsha2016@gmail.com"
    message["Subject"] = "Motivation"
    message.attach(MIMEText(quote, "plain"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="fernando.harsha2016@gmail.com",
                msg=message.as_string()  # Use the formatted message
            )
        print("Email sent!")
    except smtplib.SMTPAuthenticationError:
        print("Authentication failed. Use an App Password (not your Gmail password).")
    except Exception as e:
        print(f"Error: {e}")