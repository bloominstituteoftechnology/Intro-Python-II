# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room, item_list):
        self.name = name
        self.current_room = current_room
        self.item_list = []

    def __repr__(self):
        return f"name: {self.name}, current_room: {self.current_room}"

    def get(self, item):
        print(item)

    def drop(self, item):
        print(item)
