# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    """Rooms found within CLI text adventure game
    
    Methods:
        __init__: Initialize Room class
        get_neighbor: Return neighboring room at input direction"""

    def __init__(self, name, description):
        """Initialize Room class
        
        Args:
            name: Room name, string datatype
            description: Room description, string datatype
            
        Returns:
            Instantiated Room class

        Attributes:
            n_to: Room located directly North of instantiated Room class
            s_to: Room located directly South of instantiated Room class
            w_to: Room located directly West of instantiated Room class
            e_to: Room located directly East of instantiated Room class
            
        Usage:
            example = Room(name="Kitchen", 
                           description="Splendid aromas emanate from within")

            another_example = Room("Living Room", 
                                   "Much Netflixing occurs within these walls")

            example.n_to = another_example
            another_example.s_to = example
        """

        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None

    def get_neighbor(self, direction):
        """Return neighboring room at input direction
        
        Args:
            direction: n,s,e, or w mapping to North, South, East, and West, respectively
            
        Return:
            Name of neighboring room at cardinal direction input
            
        Usage:
            example.get_neighbor("n")"""

        if direction == "n":
            return self.n_to
        
        elif direction == "s":
            return self.s_to

        elif direction == "w":
            return self.w_to
        
        elif direction == "e":
            return self.e_to

        else:
            return None

