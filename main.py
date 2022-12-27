##################### Extra Hard Starting Project ######################
import pandas as pd
import datetime as dt
import random as rand
import os
import smtplib
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
def import_birthdays() -> dict:
    birthdays = pd.read_csv("birthdays.csv").set_index("name").to_dict(orient="index")
    print(birthdays)
    return birthdays

def get_random_letter(name:str) ->str:
    """
    Gets random letter and formats the letter by adding the recipients name
    """
    rand_file_name = rand.choice(os.listdir("letter_templates"))
    with open(f"letter_templates/{rand_file_name}", "r") as file:
        text = file.readlines()
        print(text)
        formated_line = text[0].replace("[NAME]", name)
        text[0] = formated_line
        formated_text = "".join(text)
        return formated_text





def send_birthday_mail(name:str) ->None:
    letter = get_random_letter(name)

    connection = smtplib.SMTP(host="smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user="testor.testing.the.test@gmail.com", password="")
    
    connection.sendmail(from_addr="testor.testing.the.test@gmail.com", to_addrs="tehelp.us@yahoo.com",
    
    msg=letter
    
    )

    connection.close()

def check_matching_birthday(birthdays:dict) ->None:
    for person in birthdays:
            if birthdays[person]["month"]==  dt.datetime.now().month  and birthdays[person]["day"] == dt.datetime.now().day:
                send_birthday_mail(person)
            #send_birthday_mail()

check_matching_birthday(import_birthdays())
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




