##################### Extra Hard Starting Project ######################
import pandas, smtplib, random
import datetime as dt

my_email = "email to send from"
password = "app password"

PLACEHOLDER = "[NAME]"
LETTERS = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
random_letter = random.choice(LETTERS)

data = pandas.read_csv("birthdays.csv")
data_dict = data.to_dict()
mum_bday_month = data_dict["month"][0]
mum_bday_day = data_dict["day"][0]
dad_bday_month = data_dict["month"][1]
dad_bday_day = data_dict["day"][1]

today = dt.datetime.now()
today_month = today.month
today_day = today.day



if today_month and today_day == mum_bday_day and mum_bday_month or today_month and today_day == dad_bday_day and dad_bday_month:
    with open(f"letter_templates/{random_letter}") as letter_file:
        letter_contents = letter_file.read()
        
        if mum_bday_month == today_month:
            new_letter = letter_contents.replace(PLACEHOLDER, "Mum")
        elif dad_bday_month == today_month:
            new_letter = letter_contents.replace(PLACEHOLDER, "Dad")

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="email to send to",
                                msg=f"Subject:Happy Birthday! \n\n {new_letter}")
            print("Email sent")




