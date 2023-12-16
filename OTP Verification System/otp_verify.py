import os
import math
import random
import smtplib

nums="0123456789"
OTP=""
for i in range(6):
    OTP+=nums[math.floor(random.random()*10)]
otp = OTP + " is your OTP"
msg= otp
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("Sender's Gmail ID", "Sender's App Password")
# I have removed my credentials due to security reasons but if you wish to try this you may generate your app password from google settings, Happy Learning !! 
email = input("Enter your email: ")
s.sendmail('&&&&&&&&&&&',email,msg)
x=0
for i in range(3):
    otp1=input("Enter the OTP: ")
    if otp1==OTP:
        print("Verified")
        break
    else:
        x=x+1
        if(x!=3):
            print("Please Enter the correct OTP")
        else:
            print("You have reached maximum limit, Please try again !!")
        continue
