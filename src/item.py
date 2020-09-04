class Item:
    def __init__(self, item_name, item_description):
        self.item_name = item_name
        self.item_description = item_description
        return

    def __str__(self):
        return str(self.item_name)