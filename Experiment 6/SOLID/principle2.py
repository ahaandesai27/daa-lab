"""
Open/Closed Principle
Definition: A class should be open for extension but closed for modification. 
"""

from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass
    
class EmailNotification(Notification):
    def send(self, message):
        print(f"Sending email: {message}")

class SMSNotification(Notification):
    def send(self, message):
        print(f"Sending SMS: {message}")


# In here the notification class cannot be modified but can be extended to add new types of notifications.

# notification = Notification() - will throw error
notifications = [EmailNotification(), SMSNotification()]
for notifier in notifications:
    notifier.send("Hello, World!")
