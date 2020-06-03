
'''
Creates a player object that contains a name, and what the current room location is.
'''


class Player:
    def __init__(self, name, current_room, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def _print_current_location(self):
        print(
            f'\n{self.name}, you are currently in {self.current_room.name}.\n{self.current_room.description}')

    def _print_options(self):
        print(
            f'\nThese are your current options:\nmove with [n] [s] [e] [w]\nquit the game: [q]\nget these options again [o]\n')

    def _move(self, direction_input):
        # attempt to move to the room there.
        try:
            self.current_room = self.current_room.__getattribute__(
                f'{direction_input}_to')
        # Print an error message if the movement isn't allowed.
        except:
            print(
                '\nThere is no way to go in that direction.\nPlease choose another option.\n')

    def _grab(self, item_name):
        try:
            if item_name in self.current_room.items:
                new_item = self.current_room._remove_item(item_name)
                self.inventory.append(new_item)
                print(f'You picked up a {new_item}.')
        except:
            print(f'{item_name} is not avaliable to pick up.')

    def _drop(self, item_name):
        try:
            if item_name in self.inventory:
                dropped_item = self.inventory.remove(item_name)
                self.current_room._add_item(dropped_item)
                print(f'You dropped a {item_name}.')
        except:
            print(f'{item_name} is not avaliable to drop.')

    def __str__(self):
        return f'Your name is: {self.name}\nThe current room you are in: {self.current_room}'

    def __repr__(self):
        return f'Player({self.name}, {self.current_room})'
