# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, current_room):
        self.current_room = current_room
        self.stuff = []

    def __repr__(self):
        return ('Current Location: {}'.format(self.current_room) +
                'Inventory: {}'.format(self.stuff)
                )

    def get_stuff(self, thing):
        self.stuff.append(thing)

    def drop_stuff(self, thing):
        self.stuff.remove(thing)

    def move(self, direction):
        if getattr(self.current_room, f'{direction}_to') != 'wall':
            self.current_room = getattr(self.current_room, f'{direction}_to')
        else:
            print('There is nothing for you in this direction. Where to now?')
            user = input("[n] North  [s] South  [e] East  [w] West  [q] Quit\n")
