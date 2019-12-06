# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []
    def __str__(self):
        player_inventory = f'{self.name} {self.current_room} {self.items}'
        for i in self.items:
            player_inventory += f'{i}'
        return player_inventory
    