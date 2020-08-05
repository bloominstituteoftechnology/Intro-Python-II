class Item:
    def __init__(self, name, description, id):
        self.name = name
        self.description = description
        self.id = id

    def __str__(self):
        return (f"\n    Item Name: {self.name}\n    Item Description: {self.description}\n")
