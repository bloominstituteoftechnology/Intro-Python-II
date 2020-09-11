class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def on_take(self, name):
        print(f"You have picked up {name}")

    def on_drop(self, name):
        print(f"You have dropped {name}")