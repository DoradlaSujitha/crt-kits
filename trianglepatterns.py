"""n=int(input("Enter a value: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
    print()

n = int(input("Enter a value: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

n = int(input("Enter a value: "))
for i in range(1, n + 1):
    if i % 2 == 1:
        print((str(i) + " ") * i)
    else:
        print(("* " ) * i)

n = int(input("Enter a value: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j % 2 == 1:
            print(j, end=" ")
        else:
            print("*", end=" ")
    print()

n = int(input("Enter a value: "))
for i in range(1, n + 1):
    for j in range(i):
        print(j % 2 == 0 and 1 or 0, end=" ")
    print()

n = int(input("Enter a value: "))
for i in range(1, n + 1):
    print((str(i % 2) + " ") * i)

n = int(input("Enter a value: "))
for i in range(1, n + 1):
    if i % 2 == 1:
        print(("1 " ) * i)
    else:
        print(("* " ) * i)

n = int(input("Enter a value: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j % 2 == 1:
            print("1", end=" ")
        else:
            print("*", end=" ")
    print()"""

"""#(1 44 999 4444)^2
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    for j in range(i):
        print(i * i, end=" ")
    print()

#1 14 149 14916
n=int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j*j,end=" ")
    print()

#1 23 456 78910
n=int(input("Enter a number: "))
k=1
for i in range(1,n+1):
    for j in range(i):
        print(k,end=" ")
        k+=1
    print()

#1 35 7911
n=int(input("Enter a number: "))
k=1
for i in range(1,n+1):
    for j in range(i):
        print(k,end=" ")
        k+=2
    print()

#2 46 81012
n=int(input("Enter a number: "))
k=2
for i in range(1,n+1):
    for j in range(i):
        print(k,end=" ")
        k+=2
    print()

#(1 23 456 78910)^2
n=int(input("Enter a number: "))
k=1
for i in range(1,n+1):
    for j in range(i):
        print(k*k,end=" ")
        k+=1
    print()

#(1 35 7911)^2
n=int(input("Enter a number: "))
k=1
for i in range(1,n+1):
    for j in range(i):
        print(k*k,end=" ")
        k+=2
    print()

#(2 46 811012)^2
n=int(input("Enter a number: "))
k=2
for i in range(1,n+1):
    for j in range(i):
        print(k*k,end=" ")
        k+=2
    print()

#**** *** ** *
n=int(input("Enter a value: "))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print("*",end="")
    print()

#1111 222 33 4
n=int(input("Enter a number: "))
k=1
for i in range(n,0,-1):
    for j in range(1,i+1):
        print("{:2d}".format(k),end=" ")
    k+=1
    print()

#1234 123 12 1
n=int(input("Enter a value: "))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()

#4444 333 22 1
n=int(input("Enter a value: "))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(i,end="")
    print()

#4321 432 43 4
n = int(input("Enter the number:"))
for i in range(n, 0, -1):
    for j in range(n, n - i, -1):
        print(j, end=" ")
    print()

#1111 444 99 16
n=int(input("Enter a number: "))
k=1
for i in range(n,0,-1):
    for j in range(1,i+1):
        print("{:2d}".format(k*k),end=" ")
    k+=1
    print()

#(1234 123 12 1)^2
n=int(input("Enter a number: "))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print("{:2d}".format(j*j),end=" ")
    print()

#(4444 333 22 1)^2
n=int(input("Enter a number: "))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print("{:2d}".format(i*i),end=" ")
    print()

#(4321 432 43 4)^2
n=int(input("Enter a number: "))
for i in range(n,0,-1):
    for j in range(n,n-i,-1):
        print("{:2d}".format(j*j),end=" ")
    print()"""

#right alignment

"""#* ** *** ****
n = int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(n,0,-1):
        if j<=i:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()

#1 12 123 1234
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    k=1
    for j in range(n,0,-1):
        if j<=i:
            print(k,end="")
            k+=1
        else:
            print(" ", end=" ")
    print()

#1 22 333 4444
n = int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(n,0,-1):
        if j<=i:
            print(i,end=" ")
        else:
            print(" ",end=" ")
    print()

#1 23 456 78910
n = int(input("Enter a number: "))
k = 1
for i in range(1, n + 1):
    for j in range(n, 0, -1):
        if j <= i:
            print(k, end=" ")
            k += 1
        else:
            print(" ", end=" ")
    print()

#1 14 149 14916
n=int(input("Enter a number: "))
for i in range(1,n+1):
    k=1
    for j in range(n,0,-1):
        if j<=i:
            print(k*k,end=" ")
            k+=1
        else:
            print(" ",end=" ")
    print()

#1 44 999 16161616
n=int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(n,0,-1):
        if j<=i:
            print(i*i,end=" ")
        else:
            print(" ",end=" ")
    print()

#(1 23 456 78910)^2
n = int(input("Enter a number: "))
k = 1
for i in range(1, n + 1):
    for j in range(n, 0, -1):
        if j <= i:
            print(k*k,end=" ")
            k += 1
        else:
            print(" ", end=" ")
    print()"""

#equaletral triangle

"""#* ** **
n = int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(n,0,-1):
        if j<=i:
            print("*", end=" ")
        else:
            print(" ",end="")
    print()

#1 22 333
n = int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(n,0,-1):
        if j<=i:
            print(i,end=" ")
        else:
            print(" ",end="")
    print()

#1 12 123 
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    k=1
    for j in range(n,0,-1):
        if j<=i:
            print(k,end=" ")
            k+=1
        else:
            print(" ", end="")
    print()

#1 23 456
n = int(input("Enter a number: "))
k = 1
for i in range(1, n + 1):
    for j in range(n, 0, -1):
        if j <= i:
            print(k, end=" ")
            k += 1
        else:
            print(" ", end="")
    print()

#1 00 111 0000
n=int(input("Enter a number: "))
for i in range(1, n + 1):
    for j in range(n,0,-1):
        if j<=i:
            if i%2==0:
                print(0,end=" ")
            else:
                print(1,end=" ")
        else:
            print(" ", end="")
    print()

#1 ** 111 ****
n=int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(n,0,-1):
        if j<=i:
            if i%2==0:
                print("*",end=" ")
            else:
                print(1,end=" ")
        else:
            print(" ", end="")
    print()

#* 11 *** 1111
n=int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(n,0,-1):
        if j<=i:
            if i%2==0:
                print("1",end=" ")
            else:
                print("*",end=" ")
        else:
            print(" ", end="")
    print()"""