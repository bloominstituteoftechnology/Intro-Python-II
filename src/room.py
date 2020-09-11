# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = []
    def add_item(self, item):
        self.items.append(item)
    def print_items(self):
        output = ""
        if len(self.items)== 0:
            return None
        else:
            for item in self.items:
                output += f"{item.name}"
            
        return output

    def get_direction(self, direction):
        if direction == 'n':
            return self.n_to
        elif direction == 's':
            return self.s_to
        elif direction == 'e':
            return self.e_to
        elif direction == 'w':
            return self.w_to
        else:
            return None 