class Item():
    def __init__(self, name):
        self.name = name

    def onTake(self):
        print(f"You have picked up {self.name}.")

    def onDrop(self):
        print(f"You have dropped {self.name}.")