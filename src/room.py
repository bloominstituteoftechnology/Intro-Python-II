# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items= items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        output = f'{self.name}: {self.description}\n'
        if self.s_to:
            output += 'To the south is: ' + self.s_to.name + '\n'
        if self.e_to:
            output += 'To the east is: ' + self.e_to.name + '\n'
        if self.w_to:
            output += 'To the west is: ' + self.w_to.name + '\n'
        if self.n_to:
            output += 'To the north is: ' + self.n_to.name + '\n'

        return output

    def print_items(self):
        for item in self.items:
            print(f'You find a {item.name.lower()} in this room!')

    def find_item(self, input_item):
        for item in self.items:
            if item.name.lower() == input_item.lower():
                return item
            return None
    
    def add_item(self, item):
        self.items.append(item)
        print(f'You have picked up the {item.name.lower()}')

    def remove_item(self, item):
        print(f'You habe dropped the {item.name.lower()}')
        self.items.remove(item)

    class Dark_Room(Room):
        def __init__(self, name, description, items, visibility):
            super().__init__(name, description, items)
            self.visibility = visibility
        
        def light_on(self):
            self.visibility = True