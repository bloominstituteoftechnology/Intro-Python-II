# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room
from item import Item

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []
    
    def __str__(self):
        print(f"{self.name} is currently in {self.current_room}.")

    def change_room(self, direction):
        if getattr(self.current_room, f'{direction}_to'):
            self.current_room = getattr(self.current_room, f'{direction}_to')

    def look(self):
        if len(self.current_room.items) <= 0:
            room_items = "Nothing." 
        elif len(self.current_room.items) == 1:
            room_items = f"{self.current_room.items[0].name}"
        else:
            for item in self.current_room.items:
                room_items += f"{item.name}\n"

        print(f"{self.name}, you find yourself in {self.current_room.name}. \n{self.current_room.description}")
        print(f"You see in this room the following items: {room_items}")

    def show_inventory(self):
        if len(self.inventory) <= 0:
            print(f"You haven't picked up anything yet, {self.name}.")
        elif len(self.inventory) == 1:
            print(f"You have 1 item in your inventory, {self.name}")
            print(f"{self.inventory[0].name}: {self.inventory[0].description}")
        else:
            print(f"You have {len(self.inventory)} items in your inventory.")
            for item in self.inventory:
                print(f"\n{item.name}: {item.description}")

    def select_item(self, item):
        for i in self.current_room.items:
            if i.name.lower() == str(item).lower():
                return i
            else:
                print(f"{item} not found.")
                return None
    
    def select_inventory_item(self, item):
        for i in self.inventory:
            if i.name.lower() == str(item).lower():
                return i
            else:
                print(f"{item} not found.")
                return None

    def take(self, item):
        self.inventory.append(item)
        self.current_room.items.remove(item)
        item.taken()

    def drop(self, item):
        self.inventory.remove(item)
        self.current_room.items.append(item)
        item.dropped()
        
