n=int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end="")
    print()
#method 2
n=int(input("Enter a number: "))
for i in range(1,n+1):
    print("*"*n)

n=int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,end="")
    print()

n=int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end="")
    print()

n=int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(i+64),end="")
    print()

n=int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(i+96),end="")
    print()

n=int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(j+64),end="")
    print()

n=int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(j+96),end="")
    print()

n = int(input("Enter a number: "))
for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            print(1, end="")
        else:
            print(0, end="")
    print()

n = int(input("Enter a number: "))
for i in range(n):
    for j in range(n):
        if j % 2 == 0:
            print(1, end="")
        else:
            print(0, end="")
    print()