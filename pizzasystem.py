#create a pizza ordering system that allows customer to choose pizza size and toppings
"""size = input("Enter pizza size: ")
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
print("Total Bill: $", total)"""

#allow customer to order multiple pizzas in a single order
"""num=int(input("Enter number of pizzas do you need:"))
for i in range(1, num + 1):
    print(f"Pizza {i}")
    size = input("Enter pizza size: ")
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
        else    :
            print("Invalid topping choice")
print("\n===== ORDER SUMMARY =====")
print("Total Pizzas Ordered:", num)
print("Total Bill: $", total)
print("Grand Total Bill: $", total) """

#