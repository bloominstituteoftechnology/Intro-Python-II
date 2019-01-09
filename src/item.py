class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return ": ".join((self.name, self.description))

    def on_take(self):
        print(f"{self.name} was taken.")

    def on_drop(self):
        print(f"{self.name} was dropped.")
