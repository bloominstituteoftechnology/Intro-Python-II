# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def __str__(self):
        return f'{self.current_room}'

    # def add_item(self, *args):
    #     for item in args:
    #         if item not in self.items:
    #             self.items.append(item)