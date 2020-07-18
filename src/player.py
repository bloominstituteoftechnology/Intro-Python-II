# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory
        

    def __str__(self):
        return f"<Player name: {self.name}, current_room: {self.current_room}, invenotry: {self.inventory}>"

    def pickup_items(self, *items):
        print('\nPlayer picked up items...\n')
   
        for item in items:
            self.inventory.append(item)
            print(f'{item}')
        print('\n')
        print('self.inventory', self.inventory)