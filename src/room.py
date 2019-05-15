# Implement a class to hold room information. This should have name and
# description attributes.


class Room:

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

    def __repr__(self):
        return 'You are at the %s. \n%s' % (self.name, self.description)

    def addItems(self, *items):
        self.items.append(*items)

    def showItems(self):
        statement = ''
        if len(self.items) == 0:
            statement = "You can find no items here"
        elif len(self.items) == 1:
            statement = self.items[0]
        else:
            statement += self.items[0]
            for i in range(len(self.items) - 1):
                statement += ", {}".format(self.items[i + 1])
        return statement