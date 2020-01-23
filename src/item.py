"""
Generic Item Class
"""

class Item():
    def __init__(self, id, name, desccription=None):
        self.id = id
        self.name = name
        self.description = desccription


class ItemHandler():
    def __init__(self):
        pass
    
    def move_item(self, object_1, object_2, item: Item):
        """Move item from object_1 to object_2"""
        del object_1.items[item.id]
        object_2.items.update({item.id: item})

    def place_item(self, item, receiver):
        receiver.items.update({item.id: item})