"""size=int(input("Enter the size of list:"))
Age=[]
for i in range(size):
    ele=int(input("Enter the age:"))
    Age.append(ele)
print(Age)
for i in Age:
    if(i>=1 and i<=100):
        if(i<12):
            print(f"{i}---------> $10")
        elif(i>=12 and i<=60):
            print(f"{i}---------> $15")
        else:
            print(f"{i}---------> $12")"""

#ATM MACHINE
"""pin=int(input("Enter the pin:"))
acc_bal=0
if pin==1234:
    print("Welcome to the bank")
    while True:
        print("1.Deposit")
        print("2.Withdraw")
        print("3,Balance inquiry")
        print("4.Exit")
        choice=int(input("Enter your choice:"))
        print("\n")
        if(choice==1):
            amount=int(input("Enter the amount to deposit:"))
            acc_bal=acc_bal+amount
            print(f"Dear customer your account xxxxxxxxxx1234 is credited with {amount}")
        elif(choice==2):
            amount=int(input("Enter the amount to withdraw:"))
            if(amount<acc_bal):
                print(f"Dear customer your account xxxxxxxxxx1234 is debited with {amount}")
                acc_bal=acc_bal-amount
            else:
                print("Insufficient balance.....")
        elif(choice==3):
            print(f"Dear customer your account xxxxxxxxxx1234 has {acc_bal}")
        else:
            print("Thank you....")
            break
else:
    print("You entred wrong pin")"""

#create a pizza ordering system that allows customer to choose pizza size and toppings
size = input("Enter pizza size (small/medium/large): ")
if size == "small":
    total = 10
elif size == "medium":
    total = 15
elif size == "large":
    total = 20
else:
    print("Invalid pizza size!")
    exit()
num_toppings = int(input("Enter the number of toppings: "))
for i in range(num_toppings):
    print("\nChoose a topping:")
    print("1. Cheese ($2)")
    print("2. Pepperoni ($3)")
    print("3. Olives ($5)")
    print("4. Jalapenos ($4)")
    choice = int(input("Enter topping number: "))
    if choice == 1:
        total += 2
        print("Cheese added")
    elif choice == 2:
        total += 3
        print("Pepperoni added")
    elif choice == 3:
        total += 5
        print("Olives added")
    elif choice == 4:
        total += 4
        print("Jalapenos added")
    else:
        print("Invalid topping choice")
print("\nOrder Summary")
print("Pizza Size:", size.capitalize())
print("Total Bill: $", total)