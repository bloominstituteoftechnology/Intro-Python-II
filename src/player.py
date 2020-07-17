# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def __str__(self): 
        return f'You, {self.name}, are currently in {self.current_room}'
    
    def get_item(self, name):
        # get item by passing in item name
        item = self.current_room.list_items['name']
        print(item)
        self.inventory.append(item)
    
    def get_inventory(self):
        msg = 'your current inventory: '
        msg += [item.name for item in self.inventory] 
        return msg

    # # abtract away current_room = current_room.n_to
    # def move(self, room):
    #     self.current_room == room


