"""1. Airport Check-In Management System
Problem Statement

An airport wants to automate its passenger check-in process. Passengers can check in for flights, select seats, and receive a boarding pass.

The system should store passenger details, flight information, and seat assignments, then generate a boarding pass.

Hints
Classes
Passenger
Flight
BoardingPass
Airport
Methods
register_passenger()
assign_seat()
generate_boarding_pass()
Data Structures
List → Passengers
Set → Occupied Seats
Test Case
Input
Passenger : Mason
Flight    : AI202
Seat      : 12A
Expected Output
==================================================
               BOARDING PASS
==================================================

Passenger Name : Mason
Flight Number  : AI202
Seat Number    : 12A

Status         : CHECK-IN COMPLETE"""


class Passenger:
    def __init__(self, pass_name):
        self.pass_name = pass_name
class Flight:
    def __init__(self, flight_num):
        self.flight_num = flight_num
    def assign_seat(self, seat_num):
        self.seat_num = seat_num
        return True
class BoardingPass:
    def __init__(self, passenger, flight, seat_num):
        self.passenger = passenger
        self.flight = flight
        self.seat_num = seat_num
    def generate_boarding_pass(self):
        print("=" * 50)
        print("BOARDING PASS")
        print("=" * 50)
        print(f"Passenger Name : {self.passenger.pass_name}")
        print(f"Flight Number  : {self.flight.flight_num}")
        print(f"Seat Number    : {self.seat_num}")
        print("Status: CHECK-IN COMPLETE")
        print("=" * 50)
class Airport:
    def __init__(self):
        self.passengers = []
    def register_passenger(self, passenger):
        self.passengers.append(passenger)
airport = Airport()
name = input("Passenger : ")
flight_num = input("Flight : ")
seat_num = input("Seat : ")
passenger = Passenger(name)
flight = Flight(flight_num)
airport.register_passenger(passenger)
if flight.assign_seat(seat_num):
    boarding_pass = BoardingPass(passenger, flight, seat_num)
    boarding_pass.generate_boarding_pass()
else:
    print("Seat already occupied!")