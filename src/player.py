# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, current_room):
        self.current_room = current_room
        self.bag = []

    def take_item(self, item):
        self.bag.append(item)

    def drop_item(self, item):
        self.bag.remove(item)

    def show_bag(self):
        print("Your bag contains:")
        for item in self.bag:
            print(f"{item.name}: {item.description}")

    def change_room(self, room):
        print(f"You've moved to the following room': {room.name}, {room.description}")
        self.current_room = room