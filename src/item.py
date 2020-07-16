class Item:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
    def __str__(self):
        return self.name
    def on_take(self):
        print(f"{self.name} is picked up.")
    def on_drop(self):
        print(f"{self.name} is dropped.")

class Treasure(Item):
    def __init__(self, name, desc, value):
        super().__init__(name, desc)
        self.value = value

class LightSource(Item):
    def on_drop(self):
        print(f"Dropping {self.name} is a poor decision, but it's yours to make.")