class Item:
    def __init__ (self, name, description):
        self.name = name
        self.description = description
'''Add an on_take method to Item.

Call this method when the Item is picked up by the player.

The Item can use this to run additional code when it is picked up.

Add an on_drop method to Item. Implement it similar to on_take.

Implement support for the verb drop followed by an Item name. This is the opposite of get/take.'''