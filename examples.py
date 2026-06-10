#WAP to check weather the user entered integer is a prime number or not
num = int(input("Enter a number: "))
if num <= 1:
    print("Not a prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")


#WAP to print received integer of user entered number without using built in functions
num = int(input("Enter a number: "))
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
print("Reversed number:", reverse)


#WAP to check weather the user entered integer is apalindrome or not
num = int(input("Enter a number: "))
original = num
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
if original == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")
