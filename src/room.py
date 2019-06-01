# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, item=None):
        self.name = name
        self.description = description
        self.item = []

    # def __getitem__(self):
    #     return {
    #         'name': self.name,
    #         'description': self.description
    #     }

    def __str__(self):
        return f'the {self.name}, {self.description}, {self.item}!'

    def num_of_items(self):
        if len(self.item) == 0:
            print('There are no items here for you to choose!')
