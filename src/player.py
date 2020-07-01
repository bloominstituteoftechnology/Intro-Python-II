# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.items = []

    def __str__(self):
        return f"\nNow you are in the {self.room.name}. {self.room.description}."

    def move(self, direction):
        if getattr(self.room, f"{direction}_to") is not None:
            self.room = getattr(self.room, f"{direction}_to")
            print(self)
        else:
            print("\nTry a different direction")
    
    def add_item(self, item):
        self.items.append(item)

    def take_item(self, item):
        if item in self.items:
            item.on_take()
            self.items.remove(item)
            self.add_item(item)