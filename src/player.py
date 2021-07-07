
import gameplay


class Player:

    def __init__(self, name, current_room=''):
        self.name = name
        self.current_room = current_room
        self.hp = 10
        self.inventory = {}


    def take_item(self, item_name):
        new_item = self.current_room.contents.pop(item_name)
        if not new_item:
            print(f"{item_name} is not here!")
        else: 
            print(f'You picked up {item_name}')
            self.inventory.update({item_name : new_item})


    def drop_item(self, item_name):
        new_item = self.inventory.pop(item_name)
        if not new_item:
            print(f"You dont have {item_name}!")
        else: 
            print(f"You dropped {item_name}!")
            self.current_room.contents.update({item_name : new_item})
    

    def search_room(self, cmd):
        if self.current_room.contents:
            print(f'You find {self.current_room.contents}!\n')
        else: print("You find nothing!\n")


    def change_room(self, direction):
        if hasattr(self.current_room, f'{direction[0]}_to'):
            self.current_room = getattr(self.current_room, f'{direction[0]}_to')
            gameplay.print_surroundings(self)
        else: print("You can't go that way!\n")


    def __str__(self):
        return str(vars(self))

                