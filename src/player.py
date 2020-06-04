# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, starting_room):
        self.name = name 
        self.current_room = starting_room

# #player class with location attribute

# from room import Room 

# class Player(Room): 
#     def __init__(self, current_room, name=None, description=None, n_to=None, s_to=None, e_to=None, w_to=None):
#         super().__init__(description=None, n_to=None, s_to=None, e_to=None, w_to=None)
#         self.name = name
