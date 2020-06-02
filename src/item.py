class Item:
    '''An object to be found in a room & picked up by the player'''
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        '''Called when item is picked up'''
        print(f"<You picked up the {self.name}.>")

    def on_drop(self):
        '''Called when item is dropped'''
        print(f"<You dropped the {self.name} on the floor.>")
