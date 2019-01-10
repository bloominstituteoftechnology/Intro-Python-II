# Implement a class to hold item information. This should have name and
# description attributes.


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name} - {self.description}' + '\n' + "-" * 40

    # def pick_up(self):
    #     if item_in_room:
