# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        # self.n_to = None
        # self.s_to = None
        # self.e_to = None
        # self.w_to = None
    
    def __str__(self):
        output = "\n"
        output += f"{self.name}\n"
        output += f"{self.desc}\n"
        output += "Exits to the: "
        output += f" [North] {self.n_to.name}" if hasattr(self, "n_to") else ""
        output += f" [South] {self.s_to.name}" if hasattr(self, "s_to") else ""
        output += f" [East] {self.e_to.name}" if hasattr(self, "e_to") else ""
        output += f" [West] {self.w_to.name}" if hasattr(self, "w_to") else ""
        return output