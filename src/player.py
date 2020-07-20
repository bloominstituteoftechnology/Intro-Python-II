# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def __str__(self): 
        return f'You, {self.name}, are currently in {self.current_room}'
    
    def get_item(self, item_name):
        self.inventory.append(item_name)

    
    def get_inventory(self):
        items = []
        for item in self.inventory:
            items.append(item)
        return items


