# Implement a class to hold room information. This should have name and
# description attributes.
# also add direction_to for each direction. Set to None and we will declare those when linking room in 
# the adv.py
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []

    # def __str__(self):
    #     return f"{self.name}; {self.description}; {self.items}"