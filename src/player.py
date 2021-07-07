# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room

class Player:
    def __init__( self , name , currentroom , roomdescription , hearts , items ):
        self.name = name
        self.currentroom = currentroom
        self.roomdescription = roomdescription
        self.hearts = hearts
        self.items = items

            
        
