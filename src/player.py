# Write a class to hold player information, e.g. what room they are in
# currently. Change

class Player:
    # attributes: name, current_room, items,
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def __str__(self):
        return f' \n \n Name: {self.name}. \n {self.current_room} \n Inventorty: {self.items}'

    def pick_up_item(self, item):
        self.items.append(item)
