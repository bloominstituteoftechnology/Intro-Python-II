# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room

        #print current state of player
        # def _str_(self):
        #     print(f'{self.name} is in the {self.room} room.\n')
    
    def move_player(self, direction):
        if getattr(self.room, f'{direction}_to') != None:
            self.room = getattr(self.room, f'{direction}_to')
        else:
            print("That move is not valid. Please try again.")