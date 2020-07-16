# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:

    def __init__(self, name, room, inventory):
        self.name = name
        self.room = room
        self.inventory = inventory

    def grab_item(self, item):
        """
        Adds an item to a players' inventory
        """
        self.items.append(item)
        return f"You picked up {item.name}"
    
    def drop_item(self, item):
        """
        Removes an item to a players' inventory
        """
        self.items.remove(item)
    
    def __str__(self):
        return f"{self.room}"

