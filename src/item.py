
class Item:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def on_take(self, player):
        player.items.append(self)
        player.current_room.items.remove(self)
        print(f"You have picked up {self.name}")

    def on_drop(self, player):
        player.items.remove(self)
        player.current_room.items.append(self)
        print(f"You have dropped {self.name}")
