# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:

    def __init__(self, name, location):
        self.name = name
        self.location = location

    def __repr__(self):
        return f"{name} is in {location}."

    def set_current_room(self, new_room):
        self.current_room = new_room
