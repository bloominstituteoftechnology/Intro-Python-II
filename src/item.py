class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        return

    def __str__(self):
        return (self.description)
