#single and multi level inheritance
class Vehicle:
    def __init__(self,brand,price,color,seating):
        self.brand=brand
        self.price=price
        self.color=color
        self.seating=seating
        print("Vehicle class constructor")
class Bike(Vehicle):
    def __init__(self,brand,price,color,seating,gear,milage):
        super().__init__(brand,price,color,seating)
        self.gear=gear
        self.milage=milage
        print("Bike class constructor")
v1=Bike('tata',25000,'black',4,3,45)
class Car(Vehicle):
    def __init__(self, brand, price, color, seating,gears):
        super().__init__(brand, price, color, seating)
        self.gears=gears
        print("Car class constructor")
v2=Car('Thar',120000,'black',6,4)

#multiple inheritance


#duck typing
"""class Duck:
    def walk(self):
        print("thapak thapak thapak")
class Horse:
    def walk(self):
        print("thbdak thbdak thbdak")
def myfunction(obj):
    obj.walk()
d=Duck()
myfunction(d)
h=Horse()
myfunction(h)"""


#example
"""class Engineer:
    def __init__(self):
        pass
    def work(self):
        print("Engineer is working...")
class Softwareengineer(Engineer):
    def __init__(self):
        super().__init__()
    def work(self):
        print("Softwareengineer is working....")
e1=Engineer()
e1.work()
s1=Softwareengineer()
s1.work()"""