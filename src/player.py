from src.room import Room


# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, player_name: str, current_room: Room):
        self.player_name = player_name
        self.currentRoom = current_room
