# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.items = []

    def __str__(self):
        return f"{self.items}"

    def findItemByName(self, name):
        for i in self.items:
            if i.name.lower() == name.lower():
                return i
        return None

    def addItem(self, item):
        self.items.append(item)

    def removeItem(self, item):
        self.items.remove(item)
