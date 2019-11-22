class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name}: {self.description}'

    def inspect(self):
        return "No info"


class Food(Item):
    def __init__(self, name, description, calories):
        super().__init__(name, description)
        self.calories = calories


class Gold(Item):
    def __init__(self, value):
        super().__init__('Gold', 'It is shiny!')
        self.value = value

    def inspect(self):
        return f'This gold is worth: {self.value}'
