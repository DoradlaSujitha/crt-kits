"""Problem Statement
A multiplex offers different ticket prices based on the ticket category.
Create a class Ticket with a method price() that displays:
Ticket Price: ₹150
Create a child class VIPTicket that overrides the method and displays:
Ticket Price: ₹500
Display the price for a VIP ticket.
Test Case 1
Input:VIP Ticket
Output:Ticket Price: ₹500"""

class Ticket():
    def price(self):
        print("Ticket price: Rs.150")
class VIPTicket(Ticket):
    def price(self):
        print("Ticket price: Rs.500")
ticket=VIPTicket()
ticket.price()