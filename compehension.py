"""list=[i for i in range(2,10,2)]#list comprehension
list=[i for i in range(2,10,2)]#set comprehension
print(list)
print(sorted(list))"""#sort is usedort the elements in order

"""
shallow copy:original and new list will be same because they share the same memory address
deep copy:original and new list will be different because they have different memory location
"""
#shallow copy
"""import copy
original=[1,2,3,4,5]
print(original)
new=original
print(new)
new[0]=10
print(original)
print(new)"""

#deep copy
"""import copy
original=[1,2,3,4,5]
print(original)
new=copy.deepcopy(original)
print(new)
new[0]=10
print(original)
print(new)"""

#list comprehension
list=[i for i in range(2,21,2)]
print(list)

#set comprehension
set=[i for i in range(1,11)]
print(set)

#dict comprehensio
dict={i:i*i for i in range(1,11)}
print(dict.items())
#to get power 5 or any number for the given values
dict={i:i**5 for i in range(1,11)}
print(dict.items())
