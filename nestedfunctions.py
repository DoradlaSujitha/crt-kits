"""def one():
    def two():
        print("two")
    print("one")
one()
"""

"""def washhands():
    print("washing hands")
def servefood():
    print("serving food")
def eatfood():
    washhands()
    servefood()
    print("eating food")
    washhands()
eatfood()"""

#pass function
"""def one(xyz):
    print("first function "+xyz())
def two():
    return "second function"
one(two)"""

#lamdba function
def add(a,b):
    return a+b
print(add(5,4))

add=lambda a,b:a+b
print(add(5,3))
