class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        print('You have picked up {name}'.format(name=self.name))

    def on_drop(self):
        print('You have dropped {name}'.format(name=self.name))