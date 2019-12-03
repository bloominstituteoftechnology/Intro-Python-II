class Item(object):
    def __init__(self, name, description):
      self.name = name
      self.description = description

class Key(Item):
    def __init__(self, name, description, color):
      self.color = color
      super().__init__(name, description)