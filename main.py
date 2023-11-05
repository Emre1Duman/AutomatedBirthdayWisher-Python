##################### Extra Hard Starting Project ######################
import pandas, smtplib, random
import datetime as dt

PLACEHOLDER = "[NAME]"
LETTERS = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

data = pandas.read_csv("birthdays.csv")
data_dict = data.to_dict()

mum_bday_month = data_dict["month"][0]
mum_bday_day = data_dict["day"][0]
dad_bday_month = data_dict["month"][1]
dad_bday_day = data_dict["day"][1]

today = dt.datetime.now()
today_month = today.month
today_day = today.day

if today_month and today_day == mum_bday_day and mum_bday_month:
    random_letter = random.choice(LETTERS)
    with open(f"letter_templates/{random_letter}") as letter_file:
        pass





# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




