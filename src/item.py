# this will be the base/parent class for more specialized classes declared later
class Item:
    def __init__(self, name, description):
        # name should be one word to make parsing easier down the road
        self.name = name
        self.description = description
    def on_take(self):
        print(f"You have picked up {self.name}")
    def on_drop(self):
        print(f"You have dropped {self.name}")
    def __repr__(self):
        return (f'Item Name = {self.name}, Item Description = {self.description}.')



