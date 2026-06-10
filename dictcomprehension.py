"""lang={"python","c","c++","java"}
print(lang)
lang.add("ruby")
print(lang)
ui={"html","express js","angular"}
lang.update(ui)
print(lang)
lang.remove("c")
print(lang)
lang.discard("c++")
print(lang)"""

#operators
"""set1={'doremon','motu patlu','shinchan','tom & jerry','oggy & the cockroaches'}
set2={'oggy & the cockroaches','little krishna','shinchan','heidi'}
print(set1.intersection(set2))
print(set1.union(set2))
print(set1.difference(set2))
print(set2.difference(set1))
print(set1.issubset(set2))
print(set2.issubset(set1))"""

#dictionary
"""lang={
    'UI/UX':['HTML','CSS','Javascript','Express js'],
    'Backend':['Python','Flask','Django','Pyramid','Bottle'],
    'Server':['SQL','Pl-sql','Ms-sql']
}
print(lang['UI/UX'])
print(lang['Backend'])
print(lang['Server'])
lang['Server']=['Oracel-sql']
print(lang['Server'])"""

#insertin/adding
"""std={
    101:'Scott',102:'Adams',103:'Miller',104:'James',105:'David'
}
print(std)
std[106]='xyz'
print(std)"""

#delete element(del keyword)
"""std={
    101:'Scott',102:'Adams',103:'Miller',104:'James',105:'David'
}
print(std)
std[106]='xyz'
print(std)
del std[101]
del std[106]
print(std)
#check weather 101,104,105
print(101 in std)
print(104 in std)
print(105 not in std)"""

#clear()
"""std={
    101:'Scott',102:'Adams',103:'Miller',104:'James',105:'David'
}
print(std)
std.clear()
print(std)"""

#key() and values() methods
"""std={
    101:'Scott',102:'Adams',103:'Miller',104:'James',105:'David'
}
print(std)
print(std.values())
print(std.keys())"""

#fromkeys
"""colors={

}
keys=(101,102,103,104)
values='pink'
print(colors.fromkeys(keys,values))"""

#get() method
"""std={
    101:'Scott',102:'Adams',103:'Miller',104:'James',105:'David'
}
print(std.get(101))
print(std.get(102))"""

#items() method
"""std={
    101:'Scott',102:'Adams',103:'Miller',104:'James',105:'David'
}
print(std.items())"""

#update() method
"""std={
    101:'Scott',102:'Adams',103:'Miller',104:'James',105:'David'
}
print(std.update({104:'xyz'}))"""

#pop() method
"""std={
    101:'Scott',102:'Adams',103:'Miller',104:'James',105:'David'
}
print(std.pop(102))
print(std)"""

#popitem() method
"""std={
    101:'Scott',102:'Adams',103:'Miller',104:'James',105:'David'
}
print(std.popitem())"""

#setdefault() method
"""std={
    101:'Scott',102:'Adams',103:'Miller',104:'James',105:'David'
}
print(std)
std.setdefault(107,'null')
print(std)"""

#nested list
"""list=[[10,20,30],[40,50,60],[70,80,90]]
for i in list:
    print(i)"""

#nested tuple
"""tuple=((1,2,3),(4,5,6),(7,8,9))
for i in tuple:
    print(i)"""

#nested dictionary
"""dict={
    'std1':(101,'Scott',20),
    'std2':(102,'James',30)
}
for i in dict:
    print(i,dict[i])"""

