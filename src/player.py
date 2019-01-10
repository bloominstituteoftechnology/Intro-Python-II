import os


class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.inventory = []

    def move_player(self, attribute):
        if hasattr(self.room, attribute):
            self.room = getattr(self.room, attribute)
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Can't go that way. Try another direction.\n")
