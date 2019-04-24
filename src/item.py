
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name}'

    def __lt__(self, other):
        return self.name < other.name

    def view(self):
        print(f'\n{self.name.capitalize()} – {self.description}')

    def on_take(self):
        return

    def on_drop(self):
        return