# Write a class to hold player information, e.g. what room they are in
# currently.

class Player(object):
    def __init__(self, name, room='outside'):
        self.name = name
        self.room = room
        # self.items = items
        # self._container = []

    def __str__(self):
        return f'{self.player} is now in {self.room}'

    def __repr__(self):
        return f'Player: {repr(self.player)}'

    def move(self, direction):
        directions = {'n', 's', 'e', 'w'}
        if direction not in self.directions:
            print('Cannot move in that direction!')
            return

    # def get_item(self, item):
    #     self._container.append(item)

    # def drop_item(self, item):
    #     return self._container.pop()
        