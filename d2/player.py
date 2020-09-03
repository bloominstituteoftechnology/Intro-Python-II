# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []


    def move(self, move):
        next_room = self.current_room.direction(move)
        if next_room is not None:
            self.current_room = next_room
            print(f"\nOkay, {self.name}. You're now at the {self.current_room.name}.\n{self.current_room.desc}")
        else:
            print(f"\nSorry {self.name}, can't move that direction. Unfortunately you're still at the {self.current_room.name}.")


    def get_item(self, item):
            self.inventory.append(item)


    def drop_item(self, item):
            self.inventory.remove(item)


    def view_inventory(self):
        for i in self.inventory:
            print(i.name)

    


