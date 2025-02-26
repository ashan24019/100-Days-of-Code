# import smtplib
#
# my_email = "ashanvimodh@yahoo.com"
# password = "Dr.rossgellerPHD"
#
# with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="testingashan@gmail.com",
#         msg="Subject:Hello\n\nThis is he body of my email"
#     )

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=2001, month=3, day=30)
print(date_of_birth)