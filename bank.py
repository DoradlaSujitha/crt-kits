"""Problem Statement
Different banks offer different interest rates.
Create a class Bank with a method interest_rate() that displays:
Interest Rate: 4%
Create a child class PrivateBank that overrides the method and displays:
Interest Rate: 6%
Display the interest rate of a private bank.
Test Case 1
Input:Private Bank
Output:Interest Rate: 6%"""

class Bank:
    def interest_rate(self):
        print("interest rate: 4%")
class PrivateBank(Bank):
    def interest_rate(self):
        print("interest rate: 6%")
t = input()
if t == "PrivateBank":
    obj = PrivateBank()
else:
    obj = Bank()
obj.interest_rate()