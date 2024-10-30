"""
Liskov Substitution Principle
Definition: Objects of a superclass should be replaceable with objects of its subclasses without affecting the functionality of the program.
"""
from abc import ABC, abstractmethod

class Bird(ABC):
    @abstractmethod
    def fly(self):
        pass

class Sparrow(Bird):
    def fly(self):
        print("Sparrow flying")

class Penguin(Bird):
    def fly(self):
        raise NotImplementedError("Penguins can't fly!")

def make_bird_fly(bird: Bird):
    try:
        bird.fly()
    except NotImplementedError as e:
        print(e)

# Usage
sparrow = Sparrow()
penguin = Penguin()
make_bird_fly(sparrow)   
make_bird_fly(penguin)   

# In here the function is defined for the 'Bird' type but objects of the sparrow type can also be used in the same function.
# Objects of the penguin type cannot be used as on calling the 'fly' function an error is thrown
