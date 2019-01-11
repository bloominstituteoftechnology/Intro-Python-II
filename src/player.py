import os


class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.inventory = []

    def move_player(self, attribute):
        if hasattr(self.room, attribute):
            self.room = getattr(self.room, attribute)
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Can't go that way. Try another direction.\n")

    def handle_item(self, command, item):
        if command in ('take', 'get') and self.room.check_room:
            self.inventory.append(item)
            self.room.remove_item(item)
        elif command == 'drop' and self.check_inventory:
            self.inventory.remove(item)
            self.room.add_item(item)

    def search_inventory(self):
        print('Your inventory:')
        [print(f' {item}') for item in self.inventory]
        print('\n')

    def check_inventory(self, item):
        if item in [i.lower() for i in self.inventory]:
            return True
        else:
            return False
