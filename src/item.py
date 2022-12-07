class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.hidden = False

    def __str__(self):
        return f'\nname: {self.name} \nvalue: {self.value}'

    def makeSecret(self):
        self.hidden = True