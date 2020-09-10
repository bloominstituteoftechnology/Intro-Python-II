# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    
    def __init__(self, name, description):
        self.name = name
        self.description = description
        # self.n_to = None
        # self.s_to = None
        # self.e_to = None
        # self.w_to = None
    
    def __str__(self):
        output = "\n"
        output += f"room name: {self.name}\n"
        output += f"room description: {self.description}\n\n"
        output += "Exits to the: "
        output += f"\n[North] {self.n_to.name}" if hasattr(self, "n_to") else ""
        output += f"\n[South] {self.s_to.name}" if hasattr(self, "s_to") else ""
        output += f"\n[East] {self.e_to.name}" if hasattr(self, "e_to") else ""
        output += f"\n[West] {self.w_to.name}" if hasattr(self, "w_to") else ""
        return output