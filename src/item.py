class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def on_take(self):
        print(f"You have picked up a {self.name}.\n")

    def on_drop(self):
        print(f"You have dropped your {self.name}.\n")

    def __str__(self):
        return (f"{self.name}, {self.description}")
        