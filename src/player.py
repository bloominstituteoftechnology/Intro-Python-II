# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, race, archetype, hp=50, items=[], current_room=''):
        self.name = name
        self.race = race
        self.archetype = archetype
        self.hp = hp
        self.items = items
        self.current_room = current_room

    def move(self):
        direction = {}

        if hasattr(self.current_room, 'n_to'):
            direction['N'] = self.current_room.n_to.name

        if hasattr(self.current_room, 'w_to'):
            direction['W'] = self.current_room.w_to.name

        if hasattr(self.current_room, 's_to'):
            direction['S'] = self.current_room.s_to.name

        if hasattr(self.current_room, 'e_to'):
            direction['E'] = self.current_room.e_to.name

        return direction

    def get_item(self, item):
        self.items.append(item)
        item.take(item)

    def drop_item(self, item):
        self.items.remove(item)
        item.drop(item)
