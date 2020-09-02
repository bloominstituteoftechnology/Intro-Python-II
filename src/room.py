# Implement a class to hold room information. This should have name and
# description attributes.
class Rooms:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items
        self.inventory = []

    def __str__(self):
        return f"{self.name}: {self.description}"

    def add_to_inventory_room(self, item):
        self.inventory.append(item)
        self.print_inventory()

    def remove_from_inventory_room(self, item):
        self.inventory.remove(item)
        self.print_inventory()

    
    def print_inventory(self):
        print("The rooms inventory is", [f"{c} : {p.name}: {p.description}" for c, p in enumerate(self.inventory)])
                

 