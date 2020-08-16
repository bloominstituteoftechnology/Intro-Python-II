class Item():
    def __init__(self, name, description):
        self.name = str(name).strip().replace(" ", "") # Double whammy just to be sure
        self.description = str(description)

    def on_take(self):
        print(f"You have picked up {self.description}")

    def on_drop(self):
        print(f"You have dropped {self.description}")