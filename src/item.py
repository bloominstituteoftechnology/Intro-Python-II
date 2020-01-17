

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def on_take(self):
        print(f"PICKED UP {self.name}")
    def on_drop(self):
        print(f"DROPPED {self.name}")