# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:

    def __init__(self, name, current_room, inventory: []):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def move_to(self, movement, current_location):
        attribute = movement + '_to'

        if hasattr(current_location, attribute):
            return getattr(current_location, attribute)

            print('You cannot go this direction - choose another direction')

            return current_location

    def take(self, item):
        if self.current_room.items.count(item) > 0:
            self.inventory.append(item)
            self.current_room.items.remove(item)
        else:
            print(f'The {item.name} is not here')

    def drop(self, item):
        if self.items.count(item) > 0:
            self.current_room.items.append(item)
            self.inventory.items.remove(item)
        else:
            print(f"You do not have the item {item.name} to drop")

    def print_items(self):
        if len(self.inventory) < 1:
            print("you are emptyhanded")
        else:
            print('Here is what you have: ')
            for x in self.inventory:
                print(x.name)
