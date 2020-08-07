from item import Item
# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name, description, inventory = []):
        self.name = name
        self.description = description
        self.inventory  = inventory 

    def __repr__(self):
        return (f"NAME: {self.name}, DESCRIPTION: {self.description}")

    def look_around(self):
        if len(self.inventory) == 0:
            print("\n This room doesn't have any items in it. \n")
        else:
            print ("\nItems in this room: ")
            for i in self.inventory:
                print (f" · {(i.name).upper()} \n {i.description}")

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        self.inventory.remove(item)