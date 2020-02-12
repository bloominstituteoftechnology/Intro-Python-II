class Item:
    def __init__(self, item_name):
        self.item_name = item_name

    def __str__(self):
        return f"{self.item_name}"