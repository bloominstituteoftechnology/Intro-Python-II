class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return f'{self.name}'

    def on_take(self):
        print(f'\nDescription of item: {self.description}')

    def on_drop(self):
        print(f'\nYou have dropped item: {self.name}')