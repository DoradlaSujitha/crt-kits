"""class Student():
    def __init__(self):
        print("Student object is created...!")
s1=Student()
s2=Student()"""

"""class Product():
    def __init__(self,name,price):
        print("Product object is created...")
        self.name=name
        self.price=price
        print("----------------")
p1=Product('phone',2000)
print(f"name={p1.name}")
print(f"price={p1.price}")
p2=Product('laptop',70000)
print(f"name={p2.name}")
print(f"price={p2.price}")
p3=Product('tv',20000)
print(f"name={p3.name}")
print(f"price={p3.price}")"""

"""class Student():
    def __init__(self,name,age):
        print("Student object is created...!")
        self.name=name
        self.age=age
def details(self):
    print("--------------------")
    print(f"name is {self.name}")
    print(f"age is {self.age}")
s1=Student('scott',23)
details(s1)
s2=Student('adams',33)
details(s2)
s3=Student('james',25)
details(s3)
s4=Student('arjun',22)
details(s4)"""

#example 1
"""class Mobile():
    def __init__(self,brand,price,color):
        print("Mobile object is created...!")
        self.brand=brand
        self.price=price
        self.color=color
        print("--------------------")
p1=Mobile('iphone',120000,'sliver')
print(f"brand={p1.brand}")
print(f"price={p1.price}")
print(f"color={p1.color}")
p2=Mobile('vivo',20000,'deepblue')
print(f"brand={p1.brand}")
print(f"price={p1.price}")
print(f"color={p1.color}")
p3=Mobile('iqoo',20000,'green')
print(f"brand={p1.brand}")
print(f"price={p1.price}")
print(f"color={p1.color}")
p4=Mobile('opoo',16000,'red')
print(f"brand={p1.brand}")
print(f"price={p1.price}")
print(f"color={p1.color}")
p5=Mobile('samsung',18000,'lux green')
print(f"brand={p1.brand}")
print(f"price={p1.price}")
print(f"color={p1.color}")
def details(self):
    print("--------------------")
    print(f"brand is {self.brand}")
    print(f"price is {self.price}")
    print(f"color is {self.color}")
p1=Mobile('iphone',120000,'sliver')
details(p1)
p2=Mobile('vivo',120000,'sliver')
details(p2)
p3=Mobile('iqoo',120000,'sliver')
details(p3)
p4=Mobile('opoo',120000,'sliver')
details(p4)
p5=Mobile('samsung',120000,'sliver')
details(p5)"""

#example 2
"""class Employee():
  def __init__(self,empname,empid,job,salary,dept):
    self.empname=empname
    self.empid=empid
    self.job=job
    self.salary=salary
    self.dept=dept
  print('Employee object is created....!')
def details(self):
  print(f"empname is {self.empname}")
  print(f"empid is {self.empid}")
  print(f"job is {self.job}")
  print(f"salary is {self.salary}")
  print(f"dept is {self.dept}")
e1=Employee('Aasha',1,'manager',20000,'AI')
details(e1)"""

#instance method
"""class Customer():
    def __init__(self):
        pass
    #mutator or setter method
    def set_name(self,name):
        self.name=name
    def set_id(self,id):
        self.id=id
    def set_age(self,age):
        self.age=age
    #accessor or getter method
    def get_id(self):
        print(f"id is{self.id}")
    def get_name(self):
        print(f"name is{self.name}")
    def get_age(self):
        print(f"age is{self.age}")
c1=Customer()
c1.set_id(101)
c1.set_name('Scott')
c1.set_age(23)
c1.get_id()
c1.get_name()
c1.get_age()"""


#class method (has parameters)
"""class Mobile:
    @classmethod
    def show_model(cls):
        print("Realme x")
realme=Mobile()
Mobile.show_model()"""


#static method(does not have any parameters)
"""class Mobile:
    @staticmethod
    def show_model():
        print("Realme x")
realme=Mobile()
Mobile.show_model()"""

