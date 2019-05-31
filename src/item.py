class Item:
    def __init__(self, name, description, action):
        self.name = name
        self.description = description
        self.action = action

    def __repr__(self):
        return str(self.name)
