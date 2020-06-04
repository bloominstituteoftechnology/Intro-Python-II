# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, isDark, loot = None):
        self.name = name
        self.description = description
        self.isDark = isDark
        if loot is None:
            self.loot = []
        else:
            self.loot = loot

    def __str__(self):
        return f"{self.name}: {self.description}"

    def searchRoom(self):
        print('You rummaged around and found... ')
        if len(self.loot) > 0:
            for item in self.loot:
                print(item.name)
        else:
            print('...nothing')