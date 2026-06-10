"""Problem Statement

Different vehicles have different maximum speed limits.

Create a class Vehicle with a method max_speed() that displays:

Maximum Speed: 80 km/h

Create a child class SportsCar that overrides the method and displays:

Maximum Speed: 250 km/h

Display the maximum speed of a sports car.

Test Case 1

Input

Sports Car

Output

Maximum Speed: 250 km/h
Test Case 2

Input

Vehicle

Output

Maximum Speed: 80 km/h"""

class Vehicle:
    def max_speed(self):
        print("Maximum speed: 80km/h")
class SportsCar(Vehicle):
    def max_speed(self):
        print("Maximum speed: 250km/h")
SportsCar=SportsCar()
SportsCar.max_speed()
Vehicle=Vehicle()
Vehicle.max_speed()