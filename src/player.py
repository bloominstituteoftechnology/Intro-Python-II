# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, startingroom):
        self.currentroom = startingroom
        self.playeritems = []

    def move(self, direction):

        if getattr(self.currentroom, f'{direction}_to') is not None:

            self.currentroom = getattr(self.currentroom, f'{direction}_to')
            
            print(
                f'\n~ {self.currentroom.name} ~\n\t{self.currentroom.description}\n')
        else:
            print('\nThere is no room that way!\n')

    def getitem(self, item):

        if item in self.currentroom.roomitems:

            self.playeritems.append(item)
            self.currentroom.roomitems.remove(item)

            print(f'\n\tYou got the {item}!\n')
        else:
            print(f'\n\t{self.currentroom.name} does\'t have the {item}\n')

    def dropitem(self, item):

        if item in self.playeritems:

            self.playeritems.remove(item)
            self.currentroom.roomitems.append(item)

            print(f'\n\tYou dropped the {item}!\n')
        else:
            print(f'\n\tYou don\'t have the {item} to drop!\n')

    def checkinv(self):

        inv = ', '.join(self.playeritems)

        if inv:
            print(f'\n\t{inv}\n')
        else:
            print('\n\tYou have nothing in your inventory!\n')

    def searchroom(self):

        if self.currentroom.roomitems:

            print(
                f'\n\tItem(s) in {self.currentroom.name}: {", ".join(self.currentroom.roomitems)}\n')
        else:
            print(f'\n\tThere is nothing useful in this room\n')