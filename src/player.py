# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, current_room):
        self.current_room = current_room
        self.items = []
        self.happiness = 1

    def print_item_names(self):
        return [item.name for item in self.items]

    def get_item(self, input):
        for i, item in enumerate(self.current_room.items):
            if item.name.lower() == input:
                self.items.append(self.current_room.items.pop(i))
                item.on_get(self)
                print(f"Updated inventory: {self.print_item_names()}")

    def drop_item(self, input):
        for i, item in enumerate(self.items):
            if item.name.lower() == input:
                self.current_room.items.append(self.items.pop(i))
                item.on_drop(self)
                print(f"Updated inventory: {self.print_item_names()}")

    def __repr__(self):
        return f"Player is in {self.current_room.name} \n Inventory: {self.print_item_names()}"
