# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self. current_room = current_room
        self.inventory = []

    def __str__(self):
        return f"name: {self.name}\n{self.current_room}"

    def move(self, direction):
        newRoom = self.current_room.get_room
        if newRoom is not None:
            self.current_room = newRoom
            print(self.current_room)
        else:
            print("No way to go")

    def pick_up(self, item):
        for item in self.inventory:
            if item.name == item.name:
                return item
            return None