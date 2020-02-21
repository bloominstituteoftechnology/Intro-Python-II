# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=[], n_to=None, s_to=None, e_to=None, w_to=None):
        self.name = name
        self.description = description
        self.items = items

        self.n_to = n_to
        self.s_to = s_to
        self.w_to = w_to
        self.e_to = e_to

    def __str__(self):
        return f"{self.name}\n{self.description}"
    
    def search(self):
        if len(self.items) > 0:
            output = f"\nYou find:"
            for item in self.items:
                output += f"\n- {item}"
            print(output)
        else:
            print("No items found.")

    def remove_item(self, item):
        if len(self.items) > 1:
            self.items.remove(item)
        else:
            print("Can't loot that")
    
    def add_item(self, item):
        self.items.append(item)