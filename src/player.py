# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item

class Player: 
    def __init__(self, name, room):
        self.name = name 
        self.room = room 
        self.inventory = []

    def move(self, direction): 
        if direction in ['n', 's', 'e', 'w']: 
            next_room = self.room.get_direction(direction)
            if next_room is not None:
                self.room = next_room
                print(self.room)
            else: 
                print("Oops! Can't move in that direction.")  
    
    def display_inventory(self): 
        print(f"{self.name}'s inventory: ")
        for item in self.inventory: 
            print(item) 

    def add_item(self, item):
        item.on_take()
        self.inventory.append(item)
    

    def drop_item(self, item): 
        item.on_drop()
        self.inventory.remove(item)
    