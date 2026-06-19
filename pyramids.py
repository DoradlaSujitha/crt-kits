"""#* *** *****
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    for j in range(1, 2 * n):
        if n-i+1<=j<=n+i-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# 1 222 33333 4444444
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    for j in range(1, 2 * n):
        if n-i+1<=j<=n+i-1:
            print(i, end="")
        else:
            print(" ", end="")
    print()

#1 121 12321 1234321
n = int(input("Enter a number: "))
for i in range(1,n+1):
    print("  "*(n-i),end="")
    for j in range(1,2*i):
        if j<=i:
            print(j,end=" ")
        else:
            print(2*i-j,end=" ")
    print()"""

