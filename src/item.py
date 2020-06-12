class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"

    def on_take(self):
        print(f"You have picked up the {self.name}")
        print(self.description)

    def on_drop(self):
        print(f"You have dropped the {self.name}")
        print(self.description)