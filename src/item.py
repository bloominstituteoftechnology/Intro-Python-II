class Item:

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        print(f"You've picked up a {self.name}.")

    def on_drop(self):
        print(f"You've dropped a {self.name}.")

    def __str__(self):
        return f"{self.name} - {self.description}"

    def __repr__(self):
        return f"{self.name} - {self.description}"

    
