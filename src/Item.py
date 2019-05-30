# This is the file for the Item class and other Item subclasses. Each Item will include at least a name and description.

class Item:
    def __init__(self, name, description, point_value):
        self.name = name
        self.description = description
        self.point_value = point_value

    def on_take(self):
        print(f"You have picked up the {self.name}.")

    def on_drop(self):
        print(f"You have dropped the {self.name}.")

class PuzzleItem(Item):
    def __init__(self, name, description, point_value, puzzle_solved = False):
        super().__init__(name, description, point_value)

class Treasure(Item):
    def __init__(self, name, description, point_value):
        super().__init__(name, description, point_value)

class LightSource(Item):
    def __init__(self, name, description, point_value):
        super().__init__(name, description, point_value)

    def on_drop(self):
        print("It is not wise to drop your source of light!")
