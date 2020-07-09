# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room:
    def __init__(self, name, desc, item=[]):
        self.name = name
        self.desc = desc
        self.item = item

    def __str__(self):
        x = f"{self.name} contains items: "
        for i in self.item:
            x += f"\n {i}"
        x += f"\nCurrent Location Desc: {self.desc}"
        return x
