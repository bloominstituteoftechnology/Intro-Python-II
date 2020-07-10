# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, location, inventory, victory, health):
        self.name = name
        self.location = location
        self.inventory = {}
        self.victory = False
        self.health = 100

    def is_alive(self):
        return self.health > 0

    def view_inventory(self):
        for item in self.inventory:
            print(f'{self.inventory[item]}\n')

    def get_item(self, item):
        self.inventory[item.name.lower()] = item
        del self.location.inventory[item.name.lower()]

    def drop_item(self, item):
        del self.inventory[item.name.lower()]
        self.location.inventory[item.name.lower()] = item
 