from colors import print_color
# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, name, current_room, inventory=None, knowledge=None):
        self.name = name
        self.current_room = current_room
        self.inventory = [] if inventory is None else inventory
        self.knowledge = [] if knowledge is None else knowledge

    directions = {
        'n': 'North',
        's': 'South',
        'e': 'East',
        'w': 'West'
    }

    def move(self, direction):
        try:
            room = getattr(self.current_room, f'{direction}_to')
            self.current_room = room
        except:
            print_color('red',
                        f'\n\n\nThere is no room to the {self.directions[direction]} of this room.\n\n')

    def grab_item(self, item):
        if item in self.inventory:
            print_color(
                'cyan', f'\n\nYou already have item {item.name} in your inventory.\n')
        else:
            self.inventory.append(item)
            print_color('green', f'\n\nYou picked up the {item.name}\n')

    def read_book(self, book):
        if book not in self.inventory:
            print_color('red', '\n\nYou do not have that book.')
        else:
            if book.is_read == True:
                print_color('cyan', f"\n\nYou've already read this book")
            else:
                print_color('green', f"""\n\nYou read {book.name}. You've aqcuired part of the password 
                to access treasure!""")
                book.is_read = True
                self.knowledge.append(f'{book.contents}')
