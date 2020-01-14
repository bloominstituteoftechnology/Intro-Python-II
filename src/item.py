class Item():
    def __init__(self, name):
        self.name = name

    def onTake(self, player):
        print(f"{player.name} picked up {self.name}.")

    def onDrop(self, player):
        print(f"{player.name} dropped {self.name}.")

    def onUse(self, player):
        print(f"Using {self.name}...")

    

class Rock(Item):
    def __init__(self, name):
        super().__init__(name)

    def onUse(self, player):
        super().onUse(player)
        print("Threw {self.name}")
        player.setDownItem(self)