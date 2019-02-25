# Implement a class to hold room information. This should have name and
# description attributes.

from item import Item

class Room:

    def __init__(self,name, description):
        self.name = name
        self.description = description
        self.list=[]
    def __str__(self):
        return f'name of room: {self.name} description: {self.description}'
    def listItems(self):

        for item in self.list:
            print(item)
