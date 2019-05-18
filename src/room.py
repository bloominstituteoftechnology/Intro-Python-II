# Implement a class to hold room information. This should have name and
# description attributes.


class Room:

    def __init__(self, name, description, item):
        self.name = name
        self.description = description
        self.items = [item]

    def __str__(self):
        return 'You are at the %s. \n-----------\n%s' % (self.name, self.description)

    def addItem(self, itemName):
        item = (i.name == itemName for i in self.items)
        self.items.append(item)

    def deleteItem(self, item):
        self.items.remove(item)

    def showItems(self):
        statement = ''
        if len(self.items) == 0:
            statement = "You can find no items of value here"
        elif len(self.items) == 1:
            statement = str(self.items[0])
        else:
            statement += str(self.items[0])
            for i in range(len(self.items) - 1):
                statement += ", {}".format(str(self.items[i + 1]))
        return statement