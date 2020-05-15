# Implement a class to hold room information. This should have name and
# description attributes.

""" 
The Room of Doom. Beware the Mindflayer...

Attributes:
-name
-description
-directions
    -n_to
    -s_to
    -e_to
    -w_to

"""
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
        # self.n_to = None
        # self.s_to = None
        # self.e_to = None
        # self.w_to = None
   
    
    def __str__(self):
        return f"Location: {self.name} \nDescription: {self.description}"