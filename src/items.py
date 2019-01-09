class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_add(self):
        pass

    def on_drop(self):
        pass

class Treasure(Item):
    def __init__(self, name, description):
        super.__init__(name, description)

class Lightsource(Item):
    def __init__(self, name, description):
        super.__init__(name, description)

    def on_drop(self):
        print("It's not wise to drop your source of light!")