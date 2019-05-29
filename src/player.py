class Player():
    def __init__(self, name, curr_room, inventory=[]):
        self.name = name
        self.curr_room = curr_room
        self.inventory = inventory
        return

    def add_item(self, item):
        self.inventory.append(item)
        return

    def remove_item(self, item):
        self.inventory.remove(item)
        return
