"""
Open/Closed Principle
Definition: A class should be open for extension but closed for modification. 
"""

from abc import ABC, abstractmethod
# Abstract base class module 

class Notification(ABC):
    """Defines an abstract class which can be used as a template for other types of notifications."""
    @abstractmethod
    def send(self, message):
        # Do nothing
        pass

class EmailNotification(Notification):
    """Class for email notifications, inherits from notifications template."""
    def send(self, message):
        print("Sending email:", message)

class SMSNotification(Notification):
    """Class for SMS notifications, inheritsfrom notifications template."""
    def send(self, message):
        print("Sending SMS:", message)


# In here the notification class cannot be modified but can be extended to add new types of notifications.

# Usage
notifications = [EmailNotification(), SMSNotification()]
for notifier in notifications:
    notifier.send("Hello, World!")
