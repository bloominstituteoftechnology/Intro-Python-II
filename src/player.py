# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, items):
        self.name = name
        self.current_room = current_room
        self.items = items

    def pickup_item(self, item):
        self.items.append(item)

    def drop_item(self, item):
        for i in range(0, len(self.items)):
            if self.items[i].item_name == item:
                self.items.remove(self.items[i])

    def open_inventory(self):
        for i in self.items:
            print(i)

    def __str__(self):
        return f"{self.name} is at {self.current_room}"
