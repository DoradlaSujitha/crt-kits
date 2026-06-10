class Customer:
    def __init__(self,c_name):
        self.c_name=c_name
class Movie:
    def __init__(self,movie_name,price):
        self.movie_name=movie_name
        self.price=price
class Booking:
    def __init__(self,no_of_tickets):
        self.no_of_tickets=no_of_tickets
    def calculate_amount(self,movie):
        return movie.price*self.no_of_tickets
    def generate_receipt(self,Customer,Movie):
        print("="*30)
        print("MOVIE BOOKING RECEIPT")
        print("="*30)
        print(f"Customer name: {Customer.c_name}")
        print(f"Movie name: {Movie.movie_name}")
        print(f"Ticket price: {Movie.price}")
        print(f"Tickets booked: {self.no_of_tickets}")
        print("="*30)
customer = Customer("James")
movie = Movie("Arya", 200)
booking = Booking(4)
booking.generate_receipt(customer, movie)
    