# Write a class to hold player information, e.g. what room they are in
# currently.

# NAME
# CURRENT_ROOM - change ROOM STATE based on what it is passed from adv.py 
#     initialize with default value of outside room - will have to be done when initializing object
#   


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
