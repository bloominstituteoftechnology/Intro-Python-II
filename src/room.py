# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    """Rooms found within CLI text adventure game
    
    Methods:
        __init__: Initialize Room class
        get_neighbor: Return neighboring room at input direction"""

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None

    def get_neighbor(self, direction):
        """Return neighboring room at input direction
        
        Args:
            direction: n, s, w, or e mapping to North, South, West, and East respectively
            
        Return:
            Name of neighboring room at cardinal direction input
            
        Usage:
            example.get_neighbor('n')"""

        if direction == 'n':
            return self.n_to
        
        elif direction == 's':
            return self.s_to

        elif direction == 'w':
            return self.w_to
        
        elif direction == 'e':
            return self.e_to

        else:
            return None
