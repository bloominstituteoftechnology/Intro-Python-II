# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def move(self, direction):
        if getattr(self.current_room, f'{direction}_to') is not None:
            self.current_room = getattr(self.current_room, f'{direction}_to')
        else:
            print('\nYou just hit your head on the wall... \n')

    def pickup_item(self, item):
        if self.current_room.items.count(item) > 0:
            self.items.append(item)
            self.current_room.items.remove(item)
            item.pick_up()
        else:
            print(f'{item.name} is not here...')

    def drop_item(self, item):
        if self.items.count(item) > 0:
            self.current_room.items.append(item)
            self.items.remove(item)
            item.drop()
        else:
            print(f'Can not drop what you do not have...')

    def print_items(self):
        if not self.items:
            print('You do not have any items.)
        else:
            print('You have the following items:\n ')
            for item in self.items:
                print(item.name)