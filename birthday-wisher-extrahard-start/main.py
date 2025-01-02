##################### Extra Hard Starting Project ######################
import smtplib
import pandas 
import datetime as dt 
import random


# 1. Update the birthdays.csv
now = dt.datetime.now()
to_month = now.month
to_day = now.day



# 2. Check if today matches a birthday in the birthdays.csv
MY_EMAIL = "josephtelang2004@gmail.com"
PASSWORD = "cqru rngj vqzw yogd"
today = (to_day,to_month)
print(today)
data = pandas.read_csv("birthdays.csv")
birthdays_dic = {(row.day,row.month) : row for index,row in data.iterrows()}
for key in birthdays_dic:
    
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    random_letter = random.randint(1,3)
    if key == today:
        with open(f"./letter_templates/letter_{random_letter}.txt","r") as letter:
            content = letter.read().replace("[NAME]",birthdays_dic[key]["name"])  
            content = content.replace("Angela","joseph") 
        email_to_send = birthdays_dic[key]["email"]
# 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL,password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,to_addrs=email_to_send,msg=f"subject:Happy Birthday\n\n{content}")
            
 
        










