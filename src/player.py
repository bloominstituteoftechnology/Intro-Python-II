# Write a class to hold player information, e.g. what room they are in
# currently.
from utils import clear

class Player:
    def __init__(self, location):
        self.location = location
        self.items = {}

    def list_items(self):
        items = ", ".join([name.__str__() for name in self.items])
        return items
    def move(self, direction):
        directions = ['w', 'e', 'n', 's']
        if direction not in directions:
            new_direction = input("Please enter a valid direction. (n, s, w, e)")
            self.move(new_direction)
        else:
            try:
                diff_location = self.location[f"{direction}_to"]
                self.location = diff_location
            except:
                new_direction = input("You can't move in that direction! Try again. (n, s, w, e)")
                self.move(new_direction)

    def loot(self, item_name):
        found_item = self.location.get_item(item_name)
        if found_item:
            clear()
            print(f"Yes! You got {found_item.name}.")
            self.items[found_item.name] = found_item
        else:
            print('That item is not in this room.')
            
    def drop_item(self, item_name):
        if self.items[item_name]:
            self.items.pop(item_name)
            print(f"item {item_name} successfully dropped.")
            return
        print(f"item {item_name} is not in inventory")
        
            
