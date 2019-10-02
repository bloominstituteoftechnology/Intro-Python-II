# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room

class Player:
    def __init__( self , name , currentroom ):
        self.name = name
        self.currentroom = currentroom

        print( f'{self.name} is {self.currentroom}' )

            
        
