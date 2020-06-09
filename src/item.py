class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return self.name

    def on_take(self, player):
        print(f'================ An item has been added to your inventory: {player.inventory} ================')

    def on_drop(self, player):
        print(f'============ You\'ve removed an item, here is your current inventory: {player.inventory} ============')