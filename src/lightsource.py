from item import Item


class Lightsource(Item):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_drop(self):
        print("Dropping your only source of light? Great move genius, sounds like a flawless idea\n")
        print(f"You have dropped your {self.name}.\n")