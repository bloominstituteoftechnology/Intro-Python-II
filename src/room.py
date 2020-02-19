# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None
        self.players = []
        self.items = []
        
    def __str__(self):
        display_str = ""
        display_str += f"\n{self.name}\n"
        display_str += f"\n{self.description}\n"
        display_str += f"\n{self.get_exits_string()}\n"
        return display_str
        
    def get_room_in_direction(self, direction):
        if hasattr(self, f"{direction}_to"):
            return getattr(self, f"{direction}_to")
        return None
        
    def get_exits(self):
        exits = []
        if self.n_to:
            exits.append("n")
        if self.s_to:
            exits.append("s")
        if self.w_to:
            exits.append("w")
        if self.e_to:
            exits.append("e")
        return exits
    
    def get_exits_string(self):
        return f"Exits: {', '.join(self.get_exits())}"
    
    def get_room_items(self):
        return f"Items {', '.join(self.items)}"