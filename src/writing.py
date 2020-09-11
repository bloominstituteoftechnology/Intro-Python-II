from item import Item

class Writing(Item):
    def __init__(self, name, value, text):
        super().__init__(name, value)
        self.text = text
        self.hidden = False

    def read(self):
        print(self.text)