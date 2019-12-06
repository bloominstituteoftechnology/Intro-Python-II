# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items = [], 
                n_to="nothing", e_to="nothing", s_to="nothing", w_to="nothing"):
        self.name = name
        self.description = description
        self.items = items

    def __str__(self):
        if self.items == []:
            return f"{self.description}"
        else:
            items_names = [entry.name for entry in self.items]
            items_str = ", ".join(items_names)
            return f"""{self.description}. 
            In the room, you find the following items: {items_str}"""