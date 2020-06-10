# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = 'none'
        self.s_to = 'none'
        self.w_to = 'none'
        self.e_to = 'none'
    def __str__(self):
        output = f"{self.name}: {self.description}"
        return output
    def __repr__(self):
        output = f"self.name = {self.name} ; self.description = {self.description} ; self.n_to = {self.n_to} ;  self.s_to = {self.s_to} ;  self.w_to = {self.w_to} ;  self.e_to = {self.e_to}"
        return output