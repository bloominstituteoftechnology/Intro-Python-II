# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name, description, items = []):
        self.name = name
        self.description = description
        self.items = items

    def print_description(self):
        if self.items == []:
            print(self.description)
        else:
            print(f'{self.description} You see the following items: {self.items}')

# Example abstract class left in for future reference
# from abc import ABC, abstractmethod


# class Animal(ABC):
#     def __init__(self, name, legs):
#         self.name = name
#         self.legs = legs
#     @abstractmethod
#     def speak(self):
#         pass
#     @abstractmethod
#     def species(self):
#         pass