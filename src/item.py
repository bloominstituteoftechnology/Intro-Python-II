import sys


class Item:
    '''An object to be found in a room & picked up by the player'''
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def on_take(self):
        '''Called when item is picked up'''
        print(f"<You picked up the {self.name}.>")

    def on_drop(self):
        '''Called when item is dropped'''
        print(f"<You dropped the {self.name} on the floor.>")


class CursedItem(Item):
    '''An item that kills the game if you try to drop it'''
    def on_drop(self):
        '''Called when item is dropped; kills the game'''
        super().on_drop()
        print("The floor begins to shake. Your computer screen cracks.")
        print("Blood pours out of the cracks.")
        print("YOU IS DEAD YOU IS DEAD YOU IS DEAD YOU IS DEAD LOL")
        sys.exit()
