class Item:
    def __init__(self, location, name, description, on_take, on_drop):
        self.location = location
        self.name = name
        self.description = description
        self.on_take = on_take
        self.on_drop = on_drop