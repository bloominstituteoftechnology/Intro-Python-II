# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, p_name, p_room):
        self.p_name = p_name
        self.p_room = p_room

    def __str__(self):
        return (f"from Player Class: {self.p_name} is in the {self.p_room.r_name}")

print("inside class Player",)
