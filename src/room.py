# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, items = []):
        self.name = name
        self.description = description
        self.items = items

    def print_room_info(self):
        print(f'\n{self.name}\n\n{self.description}\n')

    def check_items(self):
        if len(self.items) > 0:
            print(f'This room contains the following items:')
            for i in self.items:
                print(f'{i.name}: {i.description}')
        else:
            print('No items available in this room') 