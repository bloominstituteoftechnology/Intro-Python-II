# Write a class to hold information about Items

class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description

class LightSource(Item):
    def __init__(self, name, description, light_on=False):
        super().__init__(name, description)
        self.light_on = light_on


