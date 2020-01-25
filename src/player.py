# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, current_room, items=[]):
        self.current_room = current_room
        self.items = items

    def __str__(self):
        # print out where the player and current inventory
        output = f'Your current location: {self.current_room.name}\nYour current inventory: '
        if len(self.items)<1:
            output += f'nothing'
        else:
            for i in self.items:
                output += f"\n {i}"
        return output
    
    def take(self, item="nothing"):
        self.items.append(item)
        return f'You picked {item}'
    