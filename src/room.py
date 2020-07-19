# Implement a class to hold room information. This should have name and
# description attributes.

class Room: 
    def __init__(self, name, description, n_to=None, s_to=None, e_to=None, w_to=None, items=None):
        self.name = name
        self.description = description
        self.connections = {
           "n": n_to,
           "s": s_to,
           "e": e_to,
           "w": w_to,
        }
        self.items = items

    def __str__(self):
        for item in items:
            output  += (f"item: {item.name}")
        return output

