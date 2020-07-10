# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def pickup_item(self, item):
        return self.items.append(item)

    def try_direction(self, command):
        attribute = command + "_to"

        # see if the current room has the attribute
        # we can use a Python function called "hasattr"
        if hasattr(self.current_room, attribute):
            # use "getattr" to move to the room
            self.current_room = getattr(self.current_room, attribute)
        else:
            print("You can't go there\n")

    def __str__(self):
        return f"{self.name}"