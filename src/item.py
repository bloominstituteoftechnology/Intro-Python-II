# Item base class should have name & description(single word).

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
