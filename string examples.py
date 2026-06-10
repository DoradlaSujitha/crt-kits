"""str="PyThOn PrOgRaM"
print(str.capitalize())
print(str.casefold())
print(str.count('P'))
print(str.endswith('.'))
print(str.center(30,"*"))
print(str.expandtabs(tabsize=3))
print(str.encode())
print(str.find('RaM'))"""

#to extract name and comapany name from email
#ex scott@orscle.in
"""str="scott@orscle.in"
a=str.find('@')
b=str.find('.')
print(str[0:a])
print(str[a+1:b])"""


"""ord()-converts any character into ascii values
chr()-converts ascii(number) value into a character"""
"""for ch in range(ord('A'),ord('Z')):
    print(chr(ch))"""

"""str="       python program      "
print(str.strip())
print(str.rstrip()) #removes ending spaces
print(str.replace("",''))"""#renmoves spaces


#a company generates official email ids for employee based on their full names
#write a program that accepts an employee full name and generates






feedback=input("Enter the feedback:")
list=feedback.split()
print(max(str))