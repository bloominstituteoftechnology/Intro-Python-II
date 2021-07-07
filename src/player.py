# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []
    def move(self, direction):
        room_entered = getattr(self.current_room, f'{direction}_to')
        if room_entered is None:
            print("You can't go that way!")
        elif room_entered is not None:
            self.current_room = room_entered
            print('Your location: ', self.current_room.name)
            print(self.current_room.description)
            self.current_room.show_room_items()
            print(f'{self.current_room.get_exits_string()}, [i]')
    def print_inventory(self):
        print('You have: ')
        for item in self.items:
            print(item.name)
    
    def take_item(self,item):
        for v in self.current_room.items:
            if v.name == item:
                self.items.append(v)
                self.current_room.items.remove(v)
                print('Inventory Updated!')
            else:
                print("Can't find the item in this room")
    
    def drop_item(self,item):
        for v in self.items:
            if v.name == item:
                self.current_room.items.append(v)
                self.items.remove(v)
                print('Item dropped!')
            else:
                print("Can't find the item in your inventory")
