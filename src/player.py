# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:

    def __init__(self, playerName, current_room=None, playersItems=[], ):
        self.playerName = playerName
        self.current_room = current_room
        self.playersItems = playersItems
        

    # method for adding am item to the players items
    def addItem(self, newItem):
        self.playersItems.append()

    # method that is used for returning the list of items that the 
    # player has in his possesion
    def getPlayersItems(self):
        """
        Will return the list of items the
        player has in his possesion
        """
        return self.playersItems
    
    def getPlayersCurrentRoom(self):
        """
        The player location should be a room object
        """
        return self.current_room
    
    # Used to set the room where the player is found
    def set_current_room(self, room):
        self.current_room = room