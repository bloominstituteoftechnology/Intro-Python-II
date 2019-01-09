# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room, next_move):
        self.name = name
        self.current_room = name + 'is in' + current_room
        self.next_move = name + 'is walking' + next_move

    # def current_room(self):
    #     print("Player is currently in the current room.")
    # I think that I need to define the methods more generally and then use the specific objects to reference the generalized methods.
    # __init__ is like a constructr method.
    # def next_room(self):
    #     print("Player is moving to the next room.")
