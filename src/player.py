# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self,name, startingRoom):
        self.name = name
        self.currentRoom = startingRoom
        self.items = []
        self.capability = ['take','drop']


    def __str__(self):
        return(f'\n{self.name} with possesson:{self.items} in\n{self.currentRoom}')

    def travel(self, direction):
        nextRoom = self.currentRoom.goNextRoom(direction)
        if nextRoom is not None:
            self.currentRoom = nextRoom
            print(self.currentRoom)
        else:
            print("You cannot move in that direction.")

    def action(self, cmd):
        cmdItemList = []
        actionCmd = None
        tokenList = cmd.split()

        for token in tokenList:
            if token in self.capability :
                actionCmd = token
            else:
                cmdItemList.append(token.lower())

        if actionCmd == 'take':
            for takeItem in cmdItemList:
                itemTaken=False
                #self.currentRoom.items returns item objects list.
                # roomItem extracts item name from each item objects
                for roomItem in self.currentRoom.items:
                    if roomItem.name == takeItem:
                        self.items.append(roomItem)
                        itemTaken=roomItem.on_take()
                        break

                if not(itemTaken) :
                    print(f'***** Can not take {takeItem} which is not available in the room ******\n')
                
    
        if actionCmd == 'drop':
            for dropItem in cmdItemList:
                itemDropped=False
                #self.items contain a list of item object
                for playerItem in self.items:
                    if playerItem.name == dropItem:
                        self.items.remove(playerItem)
                        itemDropped=playerItem.on_drop()
                        break

                if not(itemDropped):
                    print(f'****Can not drop {dropItem} that is not in possession *****\n ')

        