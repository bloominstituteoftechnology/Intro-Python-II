# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, current_items):
        self.name = name
        self.current_room = current_room
        self.current_items = current_items

    def pickup_item(self, item):
        self.current_items.append(item)
        print(f'You picked up the {item.name}')

    def drop_item(self, item):
        self.current_items.remove(item)
        print(f'You dropped the {item.name}')

    def __str__(self):
        return f'{self.name} is currently located in the {self.current_room}'