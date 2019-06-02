# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, current_room):
        self.current_room = current_room
        self.items = list()

    def getInventory(self):
        if len(self.items) > 0:
            retStr = 'Your inventory contains...\n'
            for item in self.items:
                retStr += f'{item.name} : {item.description}\n'
            return retStr
        else:
            return 'Your inventory contains no items.'

    def __str__(self):
        return f'You are currently located {self.current_room}'