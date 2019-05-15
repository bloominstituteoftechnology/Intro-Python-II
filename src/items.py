class Item:

    def __init__(self, item_name):
        self.item_name = item_name

    def __repr__(self):
        return f"You now have a {self.item_name}"

    def set_current_item(self, new_item):
        self.current_item = new_item
