class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def add_item_to_inventory(self, item):
        self.inventory.append(item)
