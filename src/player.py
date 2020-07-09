# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, room, inventory=[]):
        self.room = room
        self.inventory = inventory

    def __str__(self):
        return f'{self.room} Inventory: {self.inventory}'

    def currentinv(self):
        print('Current Stash')
        for s in self.inventory:
            print(s)


    def add_weapon(self, weapon):
        self.inventory.append(weapon)

    def remove_weapon(self, weapon):
        self.inventory.remove(weapon)
