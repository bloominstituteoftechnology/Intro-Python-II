class Item (object):
    def __init__(self, name, description):
        """
        Initializing the items name and description for the Item class. 
        """
        self.name = name
        self.description = description
        self.light = False
    def __repr__(self):
        """
        returns a string describing the name and description of the item class
        """
        return f"The item name is {self.name}. Description : {self.description}."
    def on_take(self):
        """
        returns a string upon the user taking a item. 
        """
        return "This item maybe useful.."
    def on_drop(self):
        """
        returns a string upon the user dropping an item.
        """
        return "No use for this item right now but remember where you dropped it. Might come in handy later.."
class Treasure(Item):
    def __init__(self,value, name, description):
        """
        initialized value, name and description on the Treasure class. 
        """
        self.value = value
        super(Treasure,self).__init__(name, description)
    def on_take(self):
        """
        returns  string for when user takes a treasure
        """
        return "Points collected maybe time to dump this sucker."
    def on_drop(self):
        """
        returns a string for when the user drops treasure.
        """
        return "Well you have already collected the points."
    class LightSource(Item):
        def __init__(self, name, description):
            """
            Initialize the name and description for a LightSource
            """
            self.light = True
            return super(LightSource, self).__init__(name, description)
        def on_take(self):
            """
            returns a string for when a user takes a light source. 
            """
            return "Keep your light with you at all times."
        def on_drop(self):
            """
            returns a string for when a user drops a light source.
            """
            return "It's not wise to drop your source of light!"