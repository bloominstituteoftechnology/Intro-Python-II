# python item.py

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return f"Name: {self.name}, Description: {self.description}"




if __name__ == "__main__":
    item_1 = Item("Backpack", "bag to carry items")
    print(item_1)