# Write a class to hold player information, e.g. what room they are in
# currently. Change

class Player:
    # attributes: name, current_room, items,
    def __init__(self, name, current_room='outside'):
        self.name = name
        self.current_room = current_room
        self.items = []

    def __str__(self):
        return f' The players name is {self.name}. \n They are currently in : {self.current_room} room. \n This player is in possesion of the following items {self.items}'

    def pick_up_item(self, item):
        self.items.append(item)


Sam = Player('Sam')
Sam.pick_up_item('Gold')
Sam.pick_up_item('sword')
print(Sam)
