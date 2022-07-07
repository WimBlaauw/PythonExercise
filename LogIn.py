from ast import withitem
from operator import contains
from unicodedata import name

age = int(input("Please enter your age:"))
if (age < 18):
    print("Leave")

else: 
    email = input("Please enter your email:")

    password = (input("Please enter your pasword:"))
    password2 = (input("Check your password: "))

    while password != password2:
        password = (input("Re-enter password:"))
        password2 = (input("Check your password: "))

    else:
        print("You are logged in")
        
    
