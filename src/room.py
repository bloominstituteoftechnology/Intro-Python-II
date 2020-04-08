# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, n_to, s_to, e_to, w_to):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to

    # def n_to(self, n_to):
    #     self.n_to = n_to
    
    # def s_to(self, s_to):
    #     self.s_to = s_to
    
    # def e_to(self, e_to):
    #     self.e_to = e_to
    
    # def w_to(self, w_to):
    #     self.w_to = w_to
    