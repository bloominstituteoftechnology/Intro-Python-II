# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def move(self, direction):
        new_room = getattr(self.current_room, f"{direction}_to")
        if (new_room) is not None:
            self.current_room = new_room
        else:
            print("Sorry you can't move in that direction")

    def show_items(self):
        if self.items.__len__() == 0:
            return "you have no items"
        else:
            return ", ".join(list(map(lambda it: it.name, self.items)))

    def __str__(self):
        return '{self.name} {self.room}'.format(self=self)

    

