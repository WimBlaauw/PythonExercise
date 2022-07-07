import ctypes
from operator import add, mul, sub
import math

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
    ans = mul(num1,num2)
    print("Answer:" + str(ans))

elif opp == ("4"): 
    num2 = float(input("Enter second number:"))
    ans = (num1/num2)
    print("Answer:" + str(ans))

elif opp == ("5"):
    num2 = float(input("Enter second number:"))
    ans = pow(num1,num2)
    print("Answer:" + str(ans))

elif opp == ("6"): 
    ans = math.sqrt(num1)
    print("Answer:" + str(ans))
