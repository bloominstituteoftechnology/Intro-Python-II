# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.inventory = []

    def __str__(self):
        return f"Name: {self.name}\tLocation: {self.room}"

    def move_to(self, direction):
        move_room = getattr(self.room, f"{direction}_to")
        if (move_room != ""):
            self.room = move_room
        else:
            print(f'\n{"*" * 58}\n')
            print("You may not go in this direction!".center(58, ' '))


    def check_inventory(self):
        if len(self.inventory) > 0:
            print(f'\n{"*" * 58}\n')
            print(f"Your inventory currently contains:".center(58, ' '))
            for i in self.inventory:
                item = i
                print(f'{i}'.center(58, ' '))
        else :
            print(f'\n{"*" * 58}\n')
            print(f"Your inventory is currently empty".center(58, ' '))

    def on_take(self, command, item):
        if command == 'take' or 'get':
            self.inventory.append(self.room.get_item(item.lower()))
            self.room.remove_item(item.lower())
            pass

    def on_drop(self, command, item):
        if command == 'drop':
            for i in self.inventory:
                if i.name.lower() == item.lower():
                    self.inventory.remove(i)
                    self.room.add_item(i)
                    pass  
              