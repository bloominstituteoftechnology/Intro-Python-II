# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:

    def __init__(self, room):
        self.room = room
        self.items = []

    def grab_item(self, item):
        """
        Adds an item to a players' inventory
        """
        self.room.remove_item(item)
        self.items.append(item)
        return f"You picked up {item.name}"
    
    def drop_item(self, item):
        """
        Removes an item to a players' inventory
        """
        self.room.append(item)
        self.items.remove(item)
    
    def __str__(self):
        return f"{self.room}"

