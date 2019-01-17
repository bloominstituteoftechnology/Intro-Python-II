class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __repr__(self):
        return f"This room has a {self.name}, {self.description}"
    def get(self):
        return f"You took {self.name}"