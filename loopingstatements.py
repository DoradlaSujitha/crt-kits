#writw a python prg to print hello world for 5 times
"""for i in range(1,6):
    print("Hello World")
"""
#write a python prg to print the first n natural numbers
"""num=int(input("Enter a number:"))
for i in range(1,num+1):
    print(i) """

#write a python prg to print the natural numbers from n to 1
"""num=int(input("Enter a number:"))
for i in range(num,0,-1):
    print(i)"""

#write a python program to print even num till n
"""num=int(input("Enter a number:"))
for i in range(1,num+1):
    if(i%2==0):
        print(i)
print("-"*35)
for i in range(2,num+1,2):
    print(i)"""

#write a python prg to print odd num from 1 to n 
"""num=int(input("Enter a number:"))
for i in range(1,num+1):
    if(i%2!=0):
        print(i)
print("-"*35)
for i in range(1,num+1,2):
    print(i)"""

#write a python prg to calculate sum of n natural numbers
"""num=int(input("Enter a number:"))
sum=0
for i in range(1,num+1):
    sum=sum+i
print(f"The sum of first {num} numbers is",sum)"""

#write a python prg to print the factorial of n
"""num=int(input("Enter a number:"))
fact=1
for i in range(1,num+1):
    fact=fact*i
print(f"The factorial of {num} is",fact)"""

#wAP to print multiplication table of n
"""num=int(input("Enter a number:"))
for i in range(1,11):
    print(f"{num}*{i}={num}")"""

#WAP to print reversed multiplication table of m
"""num=int(input("Enter a number:"))
for i in range(10,0,-1):
    print(f"{num}*{i}={num}")"""

#WAP to print multiplication tables from 1 to n
"""num=int(input("Enter a number:"))
for i in range(1,num+1):
    print(f"Multiplication table of {i}")
    print("-"*23)
    for j in range(1,11):
        print(f"{i}*{j}={i*j}")"""


#WAP to print multiplication tables from n to 1
"""num=int(input("Enter a number:"))
for i in range(10,0,-1):
    print(f"Multiplication table of {i}")
    print("-"*23)
    for j in range(1,11):
        print(f"{i}*{j}={i*j}")"""

#WAP to print reversed multiplication tables from 1 to n
"""num=int(input("Enter a number:"))
for i in range(1,num+1):
    print(f"Multiplication table of {i}")
    print("-"*23)
    for j in range(10,0,-1):
        print(f"{i}*{j}={i*j}")"""

#WAP to print natural numbers from 1 to n
"""num=int(input("Enter a number:"))
i=1
while(i<=num):
    print(i)
    i+=1"""

