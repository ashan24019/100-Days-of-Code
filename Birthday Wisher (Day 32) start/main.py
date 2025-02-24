import smtplib

my_email = "ashanvimodh@yahoo.com"
password = "Dr.rossgellerPHD"

with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="testingashan@gmail.com",
        msg="Subject:Hello\n\nThis is he body of my email"
    )
