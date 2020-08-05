# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room, items=[]):
        self.name = name
        self.current_room = current_room
        self.items = items

    def takeItem(self, item):
        self.items.append(item)
        print(f"\n    You take the ({item.name}).\n")
        print(f"Description:\n{item.description}\n")

    def dropItem(self, item):
        self.items.remove(item)
        print(f"\n    You drop the ({item.name}).\n")

    def __str__(self):
        return (f"\n    Current Room: {self.current_room.name}\n    Room Description: {self.current_room.description}\n")
