# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room
from direction import Direction
from item import Item

class Player:
    def __init__(self, current_room: Room):
        self.name = None
        self.current_room = current_room
        self.items: [Item] = []

    def __str__(self):
        result = "You are at {self.current_room.name}.\n".format(self=self)
        return result

    def move(self, direction: Direction):

        new_room = None

        if direction == Direction.NORTH:
            new_room = self.current_room.n_to
        elif direction == Direction.SOUTH:
            new_room = self.current_room.s_to
        elif direction == Direction.EAST:
            new_room = self.current_room.e_to
        elif direction == Direction.WEST:
            new_room = self.current_room.w_to

        if new_room is not None:
            self.current_room = new_room
        else:
            print(f"⚠️  You can't go {direction.value}.\n")

    def get(self, item: Item):
        self.current_room.items.remove(item)
        self.items.append(item)
        item.picked_up()

    def drop(self, item: Item):
        self.items.remove(item)
        self.current_room.items.append(item)
        item.dropped()

    def invetory(self):
        result = "Your satchel is empty.\n"

        if len(self.items) > 0:
            result = "Your satchel contains the following items:\n"
            for i in self.items:
                result = result + f"   {i.name}\n"

        print(result)
