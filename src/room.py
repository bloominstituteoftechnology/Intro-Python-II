# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def print_name(self):
        print(f'{self.name}')

    def print_description(self):
        print(f'{self.description}')

    def outside_routes(self):
        return()