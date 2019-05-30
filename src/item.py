class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        return

    def __str__(self):
        return (self.name)

    def on_take(self):
        print('You have picked up', self.description)
        return

    def on_drop(self):
        print('You have dropped', self.description)
        return


class Treasure(Item):
    def __init__(self, name, description):
        super().__init__(name, description)
        return

    def __str__(self):
        return (self.name)

class LightSource(Item):
    def __init__(self, name, description):
        super().__init__(name, description)
        return

    def on_drop(self):
        print('It is not wise to drop your', self.name)
        return

    def __str__(self):
        return (self.name)