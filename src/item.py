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