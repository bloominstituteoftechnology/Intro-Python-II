# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, desc):
        self.desc = desc
        self.name = name

    def __src__(self):
        print('{self.name}. {self.desc}').format(self=self)
