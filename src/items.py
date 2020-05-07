class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __str__(self):
        return f"name: {self.name}, description: {self.description}"

    def on_take(self):
        print(f"You have picked up {self.name}")

    def on_drop(self):
        print(f"You have dropped {self.name}")