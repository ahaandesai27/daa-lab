"""
Single Responsibility Principle (SPR)
Definition: A class should have only one reason to change, meaning that a class should have only one job or responsibility.
"""

class OrderProcessor:
    def process(self, order):
        print("Processing order:", order)

class OrderRepository:
    def save(self, order):
        print("Saving order to database:", order)


# Each class only has one responsibility - OrderProcessor processes orders and OrderRepository saves orders to the database.

# Usage
order = {"id": 1, "items": ["apple", "banana"]}
processor = OrderProcessor()
repository = OrderRepository()
processor.process(order)
repository.save(order)
