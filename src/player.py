# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory
    def __str__(self):
        return (f"{self.name} is in the {self.current_room}.")

    def travel(self, direction):
        if hasattr(self.current_room, f'{direction}_to'):
            current_room =getattr(self.current_room, f'{direction}_to')
            self.current_room = current_room
            print(f"You have entered the {current_room}.\n")
            print(current_room.description + "\n")
        else:
            print("Wrong way!\n")
    def add_item(self, item):
        i=None
        for x in self.current_room.items:
            if x.name == item:
                i=x
        if i is None:
            print('The item is not in room')   
        else:         
            self.inventory.append(i)
            print(f'{item} is yours now!')
        # i=None
        # for x in self.current_room.items:
        #     if x.name == item:
        #         i=x
        # if i is None:
        #     print('The item name is not correct')
        # else:       
            self.current_room.items.remove(i)
            print(f'removed {i.name}')

    def drop_item(self, item):
        i=None
        for x in self.inventory:
            if x.name == item:
                i=x
        if i is None:
            print('item not in your inventory')  
        else:          
            self.inventory.remove(i)
            self.current_room.items.append(i)
    def item_inventory(self):
        if len(self.inventory) == 0:
            print('You have no items in your inventory')
        else:
            print("Your Inventory")
            for item in self.inventory:
                print(f'{item.name} ')