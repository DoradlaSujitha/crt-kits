#1111 4444 9999 16161616
n = int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print("{:2d}".format(i*i),end=" ")
    print()

#1111 3333 5555 7777
n=int(input("Enter a number: "))
k=1
for i in range(1,n+1):
    for j in range(1,n+1):
        print("{:2d}".format(k),end=" ")
    k+=2
    print()

#2222 4444 6666 8888 
n=int(input("Enter a number: "))
k=2
for i in range(1,n+1):
    for j in range(1,n+1):
        print("{:2d}".format(k),end=" ")
    k+=2
    print()

#1234 5678 9101112 
n=int(input("Enter a number: "))
k=1
for i in range(1,n+1):
    for j in range(1,n+1):
        print("{:2d}".format(k),end=" ")
        k+=1
    print()

#14916 14916 14916
n = int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print("{:2d}".format(j*j),end=" ")
    print()

#1357 1357 1357
n=int(input("Enter a number: "))
for i in range(n):
    k=1
    for j in range(n):
        print("{:2d}".format(k),end=" ")
        k+=2
    print()

#2468 2468 2468
n=int(input("Enter a number: "))
for i in range(n):
    k=2
    for j in range(n):
        print("{:2d}".format(k),end=" ")
        k+=2
    print()

#(1234 5678 9101112)^2
n=int(input("Enter a number: "))
k=1
for i in range(1,n+1):
    for j in range(1,n+1):
        print("{:2d}".format(k*k),end="  ")
        k+=1
    print()

#(1357 1357 1357)^2
n=int(input("Enter a number: "))
for i in range(n):
    k=1
    for j in range(n):
        print("{:2d}".format(k*k),end=" ")
        k+=2
    print()

#(1111 3333 5555 7777)^2
n=int(input("Enter a number: "))
k=1
for i in range(1,n+1):
    for j in range(1,n+1):
        print("{:2d}".format(k*k),end=" ")
    k+=2
    print()

#1357 9111315 17192123
n=int(input("Enter a number: "))
k=1
for i in range(1,n+1):
    for j in range(1,n+1):
        print("{:2d}".format(k),end=" ")
        k+=2
    print()

#2468 10121416 18202224
n=int(input("Enter a number: "))
k=2
for i in range(1,n+1):
    for j in range(1,n+1):
        print("{:2d}".format(k),end=" ")
        k+=2
    print()

#(2468 2468 2468)^2
n=int(input("Enter a number: "))
for i in range(1,n+1):
    k=2
    for j in  range(1,n+1):
        print("{:2d}".format(k*k),end=" ")
        k+=2
    print()

#(2468 2468 2468 2468)^2
n=int(input("Enter a number: "))
k=2
for i in range(1,n+1):
    for j in range(1,n+1):
        print("{:2d}".format(k*k),end=" ")
    k+=2
    print()

