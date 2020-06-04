class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def __repr__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def onTake(self):
        print()

    def onDrop(self):
        print()
