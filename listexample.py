#example 1
"""n=7
revenue=[]
for i in range(n):
    ele=int(input(f"Enter the revenue for day {i+1}:"))
    revenue.append(ele)
print("Total revenue:{sum(revenue)}|best day{max(revenue)}|wrost day{min(revenue)}")"""

#example2
"""queue=['Arjun','Rahul','Charan']
queue.append('Priya')
print(queue)
queue.remove('Arjun')
print(queue)
queue.insert(1,'Rani')
print(queue)"""

#example 3
"""prices=list(map(int,input("Enter your prices:").split()))
#map helps for iteration instead of loops
new_list=[]
for i in prices:
    if i>1000:
        new_list.append(i)
print(new_list)"""
#method 2
"""prices=list(map(int,input("Enter your prices:").split()))
print([i for i in prices if i>1000])"""


#example 4
"""attendence=list(map(str,input().lower().split()))
print(f"Number of absents aRE {attendence.count('absent')}")"""


#example 5
"""list=[348,299,460,610,550]
list.sort(reverse="True")
print("Ranked:",list)
print(f"Top scorer:{max(list)}")"""


#example 6
"""num=list(map(int,input('Enter the HTTP code:').split()))
print(f"last five : {num}|Critical Error Found:{True if 500 in num else False}")"""

#example 7
"""godown1=list(map(str,input('Enter the product codes:').split()))
godown2=list(map(str,input('Enter the product codes:').split()))
print("unifies inventory:",set(godown1+godown2))"""

#example 8
"""score=list(map(int,input("Enter the scores:").split()))
result=sum(score)/len(score)
print(f"The average is : {result:.2f}")"""

#example 9
"""slots=list(map(str,input("Enter the book slots:").split()))
time_slots=input("Enter the requested slots:")
print("slot already booked" if time_slots in slots else "slot is available")"""

#example 10
"""num=list(map(int,input("Enter the numbers:").split()))
print(sorted(num,reverse=True)[-3:])#least 3
print(sorted(num,reverse=True)[:3])"""#top 3

#example 11
"""num=list(map(int,input("Enter the expenses for 7 datys:").split()))
print(f"Day 1:{num[0]}|Day 2:{num[1]}|Day 3:{num[2]}|Day 4:{num[3]}|Day 5:{num[4]}|Day 6:{num[5]}|Day 6:{num[6]}")"""

#example 12
"""Dept='Tech'
Emno=4323
print(f"{Dept.upper()[:3]}-{str(Emno).zfill(5)}")"""

#example 13 pin
"""num=input("Enter the 16 digit number:")
print("**** **** ****"+num[-4])"""

#example 14 otp
"""num=list(map(str,input().split()))
for i in num:
    if i.isdigit():
        print(i)"""

#example 15 
"""num=list(map(str,input().split()))
for i in num:
    if i.isalnum():
        print(i)
        print("valid IFSC code")
    else:
        print("Invalid IFSC code")"""

