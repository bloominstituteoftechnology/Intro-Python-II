# Write a class to hold player information, e.g. what room they are in
# currently.

from item import Item

class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.items = []

    def change_player_room(self, room):
        self.room = room

    def pick_up_item(self, item):
        question = input(f'\nAre you sure you want to pick up {item.name} ?  Y/N ')
        if question.lower() == 'y':
            item.on_take()
            self.items.append(item)
        else:
            pass

    def drop_off_item(self, item):
        question = input(f'\nAre you sure you drop {item.name} ?  Y/N ')
        if question.lower() == 'y':
            item.on_drop()
            self.items.remove(item)
        else:
            pass

