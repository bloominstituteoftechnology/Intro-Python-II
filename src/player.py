# Write a class to hold player information, e.g. what room they are in
class Player:
    def __init__(self, current_room):
        self.current_room = current_room
    
    def __repr__(self):
        return f"Player is in {self.current_room}"
# currently.
