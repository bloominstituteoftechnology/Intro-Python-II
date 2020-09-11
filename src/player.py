# Write a class to hold player information, e.g. what room they are in
# currently.

# Needed to add inventory to the class so the player can hold mult. items

class Player:
    def __init__(self, name, current_room, inventory = []):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def hunt_for_items(self):
        items = self.current_room.items
        if items != None:
            return f' Look! There is a {items}.'
        else:
            return "Nothing here, better keep looking"