"""
Dependency Inversion Principle (DIP)
Definition: High-level modules should not depend on low-level modules; both should depend on abstractions.
"""
from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def save(self, data):
        pass

class MySQLDatabase(Database):
    def save(self, data):
        print("Saving data to MySQL:", data)

class MongoDB(Database):
    def save(self, data):
        print("Saving data to MongoDB:", data)

class DataHandler:
    def __init__(self, db: Database):
        self.db = db

    def save_data(self, data):
        self.db.save(data)

# The mongodb and mysql handler only depend on the database interface, and not on each other 
# We should be able to switch between two databases without changing the handler's code
# Usage
mysql_db = MySQLDatabase()
mongo_db = MongoDB()
handler = DataHandler(mysql_db)
handler.save_data("Order Data")  
handler = DataHandler(mongo_db)
handler.save_data("User Data")
