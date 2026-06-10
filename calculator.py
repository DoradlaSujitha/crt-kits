def add(a,b):
    print(f"Addition of {a} and {b} is {a+b}")
def sub(a,b):
    print(f"Subtraction of {a} and {b} is {a-b}")
def mul(a,b):
    print(f"Multiplication of {a} and {b} is {a*b}")
def div(a,b):
    print(f"Division of {a} and {b} is {a/b}")
def mod(a,b):
    print(f"Modular division of {a} and {b} is {a%b}")
while True:
    print("1,Adition")
    print("2,Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Modular division")
    print("6.Exit")
    print("-"*30)
    choice = int(input("Enter your choice:"))
    if choice == 6:
        break
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    if choice == 1:
        add(a,b)
    elif choice == 2:
        sub(a,b)
    elif choice == 3:
        mul(a,b)
    elif choice == 4:
        div(a,b)
    elif choice == 5:
        mod(a,b)
    print("\n")