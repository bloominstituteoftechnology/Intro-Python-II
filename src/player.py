# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, inventory, current_room=None, score=0):
        self.name = name
        self.inventory = inventory
        self.current_room = current_room
        self.score = score

    def __str__(self):
        return self.current_room

    def take_item(self, item):
        self.inventory.append(item)
    
    def drop_item(self, item):
        self.inventory.remove(item)

    def view_inventory(self):
        print(f'{self.name} is currently holding: ')
        for item in self.inventory:
            print(f'{item.name.capitalize()}')

    def find_item(self, input_item):
        for item in self.inventory:
            if item.name.lower() == input_item.lower():
                return item
        return None

    def get_score(self):
        print(f'Current Score: {self.score}')

    def add_score(self, points):
        self.score = self.score + points