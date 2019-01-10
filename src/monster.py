class Monster():
    def __init__(self, name, description, health, weapon):
        self.name = name
        self.description = description
        self.health = health
        self.weapon = weapon

    def on_attack(self):
        print("You have picked up a {self.description}".format(self = self))

    def def_attack(self):
        print("You have ")