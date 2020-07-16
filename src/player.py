# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:
    def __init__(self, current_room=None):
        self.current_room = current_room
    

#player_1 = Player('outside')
#print(player_1.current_room)
#print(player_1.description)