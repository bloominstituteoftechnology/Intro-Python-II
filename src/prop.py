from item import Item


class Prop(Item):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.hidden = False     # set to True if this Prop is inside a Fixed item
        self.held = False

    def __str__(self):
        if self.held:
            return f'You are holding {self.a_or_an()} {self.name}. {self.description}.'
        else:
            return f'There is {self.a_or_an()} {self.name} here. {self.description}.'
