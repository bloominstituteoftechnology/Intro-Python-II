class Item():
    def __init__(self, name, description, damage, type):
        self.name = name
        self.description = description
        self.damage = damage
        self.type = type

    def on_take(self):
        print("You have picked up a {self.description}".format(self = self))

    def on_drop(self):
        print("You have dropped your {self.name}".format(self = self))