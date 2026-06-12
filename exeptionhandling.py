"""print("Program stars")
a=10
print("a=",a)
try:
    print(a/0)
except ZeroDivisionError as e:
    print("Not possible to divide with zero if u divide it gives ",e)
print("program ending")"""

"""age=int(input("Enter your age: "))
if age>18:
    print("Eligible to vote")
else:
    raise Exception('Not eligible to vote')"""

"""balance=3000
try:
    amount=int(input("Enter withdrawal amount: "))
    if amount>balance:
        raise ValueError("Insufficient Balance")
    print("Withdrawal Successful")
except ValueError as e:
    print("Transaction Failed:")"""



"""try:
    monthly_salary=float(input("Enter monthly salary:"))
    if monthly_salary<=0:
        raise ValueError
    annual_salary=monthly_salary
    print("Annual Salary:",annual_salary)
except ValueError:
    print("Please enter a valid salary amount")"""

"""pin=input("Enter your Password:")
try:
    if pin=='1234':
        print("Login is successful")
    else:
        raise TypeError("Incorrect password")
except TypeError as e:
    print(e)"""


#using finally
"""a=10
try:
    print(a)
finally:
    print("Finally Block Code")"""