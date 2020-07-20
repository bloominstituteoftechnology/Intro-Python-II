# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def __str__(self): 
        return f'You, {self.name}, are currently in {self.current_room}'
    
    def get_item(self, item_name):
        print("itesm", self.current_room.list_items())
        # print(self.current_room.items[item_name])
        # print(index)
        # index = self.current_room.list_items().index(item_name)
        # item = self.current_room.items[index]
        # self.current_room.items.remove(item)
        # self.inventory.append(item)
        # print(self.inventory)

    
    def get_inventory(self):
        msg = 'your current inventory: '
        for item in self.inventory:
            msg + item.name
        print(msg)
        return self.inventory


    # def add_item(self, item):
    #     self.invetory.append(item)
