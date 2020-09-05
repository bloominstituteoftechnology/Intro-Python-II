# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, room):
        self.room = room
        self.items = []

    def changeRoom(self, mov):
        if mov == 'q':
            exit()
        elif mov == 'n':
            if hasattr(self.room, 'n_to'):
                self.room = self.room.n_to
            else:
                print("North is not a valid direction")
        elif mov == 'e':
            if hasattr(self.room, 'e_to'):
                self.room = self.room.e_to
            else:
                print("East is not a valid direction")
        elif mov == 's':
            if hasattr(self.room, 's_to'):
                self.room = self.room.s_to
            else:
                print("South is not a valid direction")
        elif mov == 'w':
            if hasattr(self.room, 'w_to'):
                self.room = self.room.w_to
            else:
                print("West is not a valid direction")
        else:
            print("[Error] Unexpected Input:", mov)
            print("Expected: n, e, s, w, q")

    def modifyItem(self, command):
        args = command.split() # List containing take/drop and item name
        if len(args) < 2:
            print('[Error]: Unexpected Input:', command)
        else:
            modifier = args[0]
            itemname = ""
            # Full itemname if spaces are included eg 'Gold Coin' input
            # NOTE Needs to be fixed
            if len(args) > 2:
                for arg in args:
                    itemname += f"{arg}"
            else:
                itemname = args[1]
            # Check item exists in room
            item = None
            for i in self.room.items:
                if i.name == itemname:
                    item = i
                    break
            if item == None:
                # Check item exists on player
                for i in self.items:
                    if i.name == itemname:
                        item = i
            # If item doesn't exist, print error
            if item == None:
                print(f"[Error]: Could not find item named \"{itemname}\"")
                return
                
            # Check modifier
            if modifier == 'take':
                self.room.items.remove(item)
                self.items.append(item)
                print('You picked up the', item.name)
            elif modifier == 'drop':
                self.items.remove(item)
                self.room.items.append(item)
                print('You dropped the', item.name)
            else:
                print(f'[Error]: invalid modifier {modifier}, use take/drop.')