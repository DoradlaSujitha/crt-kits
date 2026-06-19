#1.1,4,7,10,13,16,19...n
n=int(input("Enter a number: "))
for i in range(n):
    print(1+3*i,end=" ")

#2.1,4,9,16,25,36,49,64,81,100...n
n=int(input("Enter a number: "))
for i in range(1,n+1):
    print(i*i,end=" ")

#3.0,1,1,2,3,5,8,13,21...n
n=int(input("Enter a number: "))
a,b=0,1
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b

#4.0,5,10,15,20,25,30..n
n=int(input("Enter a number: "))
for i in range(1,n+1):
    print(5*i,end=" ")

#5.2,3,5,7,11,13,17,19,23...n
n = int(input("Enter a number: "))
count = 0
num = 2
while count < n:
    is_prime = True
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
        count += 1
    num += 1

#6.A--->65,B---->66.......Z--->90
for i in range(65,91):
    print(chr(i),"--->",i)

#7.1,3,5,7,9,11.......n
n=int(input("Enter a number: "))
for i in range(n):
    print(2*i+1,end=" ")

#8.2,4,6,8,10,12.....n
n=int(input("Enter a number: "))
for i in range(1,n+1):
    print(2*i,end=" ")