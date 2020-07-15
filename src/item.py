# This is the fle that will contain the class about the items

class Item:

    def __init__(self, name, description):
        self.name = name
        self.description = description

    # adding the on_take method in the item class
    def on_take(self):
        return f"You have picked up {self.name}"

    def on_drop(self):
        return f"You have drop the{self.name}"


# Making a new class that will be a subclass of the Item class
class LightSource(Item):

    def __init__(self, name, description):
        super().__init__(name, description)

    
    # method that will override the item on_drop
    def on_drop(self):
        return f"It is not wise to drop your light source."

