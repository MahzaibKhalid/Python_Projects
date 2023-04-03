import os
import random
import smtplib

def automatic_emails():
    user= input("Enter the Username:")
    email=input("Enter your Email:")
    message = (f"Dear {user}, Welcome to Code With Mahzaib!")
    s= smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login('mahzaibkhalid235@gmail.com','dxscjtctpgskfrnm')
    s.sendmail("&&&&&&&&&&&",email,message)
    print("Email Sent!")
    

automatic_emails()