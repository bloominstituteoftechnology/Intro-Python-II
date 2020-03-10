# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    """

    """
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room

    def travel(self, direction):
        next_room = getattr(self.current_room, f"{direction}_to")
        if next_room != None:
            self.current_room = next_room
            print("\n---------New Room---------")
            print(self.current_room.name)
            print(self.current_room.description)
            print("--------------------------")
        else:
            print("\nYou can't move that direction\n")

