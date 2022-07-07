from ast import withitem
from operator import contains
from unicodedata import name
import ctypes
from operator import add, mul, sub
import math
from traceback import print_list
from turtle import position
import random

print("\n1.Calculator \n2.Random Number Generator \n3.Capital Letter \n4.Log in \n5.Password Guesser \n6.Online Count")
choice = input("Choose your program:")
if choice == 1:

    num1 = float(input("Enter first number:"))
    print("Select the operatorion \n1.Addition \n2.Subtraction \n3.Multiplication \n4.Division \n5.Power \n6.Square route")
    opp = input("Choose out of (1/2/3/4/5/6):")

    if opp == ("1"): 
        num2 = float(input("Enter second number:"))
        ans = add(num1,num2)
        print("Answer:" + str(ans))

    elif opp == ("2"): 
        num2 = float(input("Enter second number:"))
        ans = sub(num1,num2)
        print("Answer:" + str(ans))

    elif opp == ("3"): 
        num2 = float(input("Enter second number:"))
        ans = (num1*num2)
        print("Answer:" + str(ans))

    elif opp == ("4"): 
        num2 = float(input("Enter second number:"))
        ans = mul(num1,num2)
        print("Answer:" + str(ans))

    elif opp == ("5"):
        num2 = float(input("Enter second number:"))
        ans = pow(num1,num2)
        print("Answer:" + str(ans))

    elif opp == ("6"): 
        ans = math.sqrt(num1)
        print("Answer:" + str(ans))

elif choice == 2:

    minimum = input("Minimum value:")
    maximum = input("Maximum value:")

    def random_number():
        n_list = [*range (int(minimum), int(maximum))]
        print(random.choice(n_list))

    random_number()

elif choice == 3:

    def capitalpos(word):
        capitals = [index for index in range (len(text)) if text[index].isupper()]
        print(capitals)
 
    text = input("Please enter a word or sentence:")
    capitalpos(text)  

elif choice == 4:

    age = int(input("Please enter your age:"))
    if (age < 18): print("Leave")

    else: 
        email = input("Please enter your email:")

        password = (input("Please enter your pasword:"))
        password2 = (input("Check your password: "))

        while password != password2:
            password = (input("Re-enter password:"))
            password2 = (input("Check your password: "))

        else: print("You are logged in")

elif choice == 5:

    password = "hello"
    passwordprompt = input("Enter password:")

    while passwordprompt != password:
        passwordprompt = input("Enter password:")
        if passwordprompt == password: break

elif choice == 6:
    online_count = 0 
    statuses = {
        "alice": "online",
        "bob": "offline",
        "eve": "offline", 
    }

    for value in statuses.values(): 
        if value == "online":
            online_count += 1
        if online_count == 0:
            print("There are no users online.")
        elif online_count == 1:
            print("There is 1 user online")
        else:
            print("There are " + str(online_count) + " users online.") 
