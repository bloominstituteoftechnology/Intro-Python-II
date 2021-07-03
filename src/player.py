# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, room, inventory, health, onhand_weapon):
        self.room = room
        self.inventory = inventory
        self.health = health
        self.onhand_weapon = onhand_weapon

    def __str__(self):
        return """\n
                  Health: {self.health}
                  Current Location: {self.room.name}
                  Room Description: {self.room.description}""".format(self = self)
