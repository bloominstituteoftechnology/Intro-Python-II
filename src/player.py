# Write a class to hold player information, e.g. what room they are in
# currently.
#test 
#test 
class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
        self.items = []

    def travel(self, direction):
        next_room = getattr(self.current_room, f"{direction}_to")
        if next_room is not None:
            self.current_room = next_room
            print(self.current_room)
            print("Items: '{}'".format(", ".join([item.name for item in self.current_room.items])))
        else:
            print("You cannot move in that direction")
    
    def take(self, item_name):
        item = self.current_room.drop(item_name)
        self.items.append(item)
        item.on_take()
        return item

    def drop(self, item_name):
        item = self.find(item_name)
        self.items.remove(item)
        self.current_room.take(item)
        item.on_drop()
        return item

    def find(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return item
        