# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:

    def __init__(self, name, currentLoc):
        self.name = name
        self.currentLoc = currentLoc
        self.items = []


    def __repr__(self):
        return self.name

    def addItem(self, item):
        self.items.append(item)

    def deleteItem(self, item):
        self.items.remove(item)

    def showItems(self):
        statement = ''
        if len(self.items) == 0:
            statement = "You are holding nothing"
        elif len(self.items) == 1:
            statement = str(self.items[0])
        else:
            statement += str(self.items[0])
            for i in range(len(self.items) - 1):
                statement += ", {}".format(str(self.items[i + 1]))
        return statement