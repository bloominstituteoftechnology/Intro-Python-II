# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, current_room):
        self.current_room = current_room
        self.inventory = []

    def take_item(self, item):
        self.inventory.append(item)

    def drop_item(self, item):
        self.inventory.remove(item)

    def show_inventory(self):
        print("You have the following items in your inventory:")
        for item in self.inventory:
            print(f"{item.name}: {item.description}")

    def move_to(self, room):
        if self.current_room != room:
            self.current_room = room
            print(f"You have now entered: {room.name}, {room.description}")
