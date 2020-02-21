class Item:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"item name is{self.name}"
