# Implement a class to hold room information. This should have name and
# description attributes.


class Room():
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def __repr__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def canMoveTo(self, direction):
        dirStr = f"{direction}_to"
        for key in self.__dict__.keys():
            if dirStr == key:
                return True
        return False

    def getRoom(self, direction):
        dirStr = f"{direction}_to"
        for key in self.__dict__.keys():
            if dirStr == key:
                return self.__dict__[key]
