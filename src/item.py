class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self, player):
        print(f'You have picked up a {self.name}')
        player.items.append(self)
        player.current_room.items.remove(self)

    def on_drop(self, player):
        print(f'You have dropped a {self.name}')
        player.items.remove(self)
        player.current_room.items.append(self)