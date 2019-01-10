# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.items = []

    def addItem(self, item):
        self.items.append(item)

    def removeItem(self, item):
        if len(self.items) > 0:
            for i in self.items:
                if i.name == item:
                    self.items.remove(i)
        else:
            print("Item can not be removed.")
