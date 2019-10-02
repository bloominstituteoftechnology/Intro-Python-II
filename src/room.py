# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__( self , currentroom , description ):
        self.currentroom = currentroom
        self.description = description
        self.direction = direction

        if ( direction == 'n_to' ):
            print( 'ooga' )


    def __str__(self):
        return ''+self.currentroom+' '+self.description+ ')'
