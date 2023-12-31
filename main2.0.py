##################### Birthday Wisher Project ######################
import pandas, smtplib, random
import datetime as dt

my_email = "email to send from"
password = "app password"

today  = (dt.datetime.now().month, dt.datetime.now().day)
data = pandas.read_csv("birthdays.csv")

# birthdays_dict = {
#     (birthday_month, birthday_day): data_row
# }

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday! \n\n {letter_file}")
        print("Email sent")
