# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = {}
        self.victory = False
        self.hp = 100

    def is_alive(self):
        return self.hp > 0

    def view_inventory(self):
        for item in self.inventory:
            print(f'{self.inventory[item]}\n')

    def get_item(self, item):
        self.inventory[item.name.lower()] = item
        del self.current_room.inventory[item.name.lower()]

    def drop_item(self, item):
        del self.inventory[item.name.lower()]
        self.current_room.inventory[item.name.lower()] = item
