""" QN1. Write a program that asks the user for their name and age , then prints a sentece like "Hello Shradha ,you are 21 years old!" """
name = input("Enter your name: ")
age = int(input("Enter your age: " ))
print(f"Hello {name} ,You are {age} years old!")

"""Q2 Take two numbers as input from the user and print their sum, difference, product,andquotient."""

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"the sum of {num1} and {num2} is {num1 + num2}.")
print(f"the difference between {num1} and {num2} is {num1 - num2}.")
print(f"the product of {num1} and {num2} is {num1 * num2}.")

'''# Q3. Ask the user to enter two integers and one float Convert them all to floats and print their average.'''

intnum1 = int(input("Enter first integer number : "))
intnum2 = int(input("Enter second integer number: "))
floatnum = float(input("Enter float number: "))
avg =( intnum1 + intnum2 + floatnum)/3
print(avg)

"""Q4 The user enters a string containing a number(e.g."45").Convert it to
•aninteger
•afloat
•astring again Print all three values with their types"""
str2 = input("Enter a number: ")
int_num = int(str2)
float_num = float(str2)
str1 = str(str2)
print(f"{int_num} {type(int_num)}")
print(f"{float_num} {type(float_num)}")
print(f"{str1} {type(str1)}")

"""Q5. Take a decimal number as input (like 45.78) and output its:
•integer part - 45 
•fractional part - .78"""

dec = 45.78
print(f"integer part - {int(dec)}")
print(f"fractional part - {dec - int(dec)}")