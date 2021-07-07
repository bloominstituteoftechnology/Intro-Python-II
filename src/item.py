class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return f"(self.name), (self.description)"

    def on_get(self):
        print("You acquired " + self.name)

    def on_drop(self):
        print("You dropped " + self.name)