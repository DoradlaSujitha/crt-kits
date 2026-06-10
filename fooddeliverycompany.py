class Customer:
    def delivery_charges(self):
        print("Delivery charge of 50")
class PrimeCustomer(Customer):
    def delivery_charges(self):
        print("Delivery charge of 20")
customer=PrimeCustomer()
customer.delivery_charges()