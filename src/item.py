class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return self.name

    def pick_up(self):
        return f'You picked up {self.name}!'

    def drop_it(self):
        return f'You dropped {self.name}!'

    def look(self):
        return f'Item: {self.name}\nDescription: {self.description}'
