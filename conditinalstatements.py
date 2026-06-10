#write a python program to read age input from the user and check weather the age is valid to vote or not
"""age=int(input("Enter your age: "))
if(age>=18):
    print("you are eligible to vote")
else:
    print("ypu are not eligible to vote")

#ternary operator
res="eligible" if age>=18 else"not eligible"
print("you are",res,"to vote")"""

#write a python prg to read a int value asi/p from user and check weather it is + or - or zero
"""num=int(input("Enter a number:"))
if(num>0):
    print(f"{num} is positive")
elif(num<0):
    print(f"{num} is negative")
else:
    print(f"{num} is zero")"""

 #write a python prg to read 2 int values as input and find the largest number
"""num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
if(num1>num2):
    print(f"{num1} is greater")
else:
    print(f"{num2} is greater")
"""
#write a python prg to read the month number as i/p from the user and check weather 
# it is a valid month number or not
"""month=int(input("Enter month number:"))
if(month>=1 and month<=12):
    print(f"{month} is valid")
else:
    print(f"{month} is invalid")"""

#write a python prg to read month num from the user and print the respective
# number of days present in the month
"""month=int(input("Enter month number:"))
if(month in [1,3,5,7,8,10,12]):
    print("31 days")
elif(month in [4,6,9,11]):
    print("30 days")
elif(month==2):
    print("28 or 29 days")
else:
    print("Invalid month")"""

#write a python prg to check weather the user entered num is even or odd
"""num=int(input("Enter a number:"))
if(num%2==0):
    print(f"{num} is even")
else:
    print(f"{num} is odd")"""

#write a python prg to check weather the user entered  year is a leap year or not
"""year=int(input("Enter a year:"))
if(year%4==0 and year%100!=0) or (year%400==0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")"""

#write a python prg to read 3 int values and find the largest number
"""a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
if(a>=b) and (a>=c):
    print(f"{a} is largest")
elif(b>=a) and (b>=c):
    print(f"{b} is largest")
else:
    print(f"{c} is largest")"""


#write a python prg to read 3 int values and find the smallest number 
"""a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
if(a<=b) and (a<=c):
    print(f"{a} is smallest")
elif(b<=a) and (b<=c):
    print(f"{b} is smallest")
else:
    print(f"{c} is smallest")"""


#write a pyhton prg to read 2 int values and find the smallest number
"""a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
if(a<b):
    print(f"{a} is smallest")
else:
    print(f"{b} is smallest")"""


#write a python prg to read 3 int values and find the middle number
"""a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))"""

# a supermarket ofers 10% discount if the total bill is greater than 500
"""totalbill=int(input("enter total amount:"))
if(totalbill>500):
    print("discount applicable")
else:
    print("no discount")
"""
marks=int(input("Enter marks:"))
if(marks>=35):
    print("pass")
else:
    print("Fail")