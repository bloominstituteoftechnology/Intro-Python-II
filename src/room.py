# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name, text, items, is_hungry):
        self.name = name
        self.text = text
        self.items = items
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None
        self.is_hungry = is_hungry
        
        def add_item(self, item):
            self.items.append(item)
        
        def get_items_list(self):
            if (self.items):
                return [i.name for i in self.items]
            else:
                return []

        # def print_items(self):
        #     print('Items: {self.items}')

        def get_room_dir(self, direction):
            if direction == "n":
                return self.n_to
            elif direction == "s":
                return self.s_to
            elif direction == "e":
                return self.e_to
            elif direction == "w":
                return self.w_to
            else:
                return None
        
        def connect_rooms(self, destination_room, direction):
            if direction == "n":
                self.n_to = destination_room
                destination_room.s_to = self
            elif direction == "s":
                self.s_to = destination_room
                destination_room.n_to = self
            elif direction == "e":
                self.e_to = destination_room
                destination_room.w_to = self
            elif direction == "w":
                self.w_to = destination_room
                destination_room.e_to = self
            else:
                print("Invalid Direction")

    def display_items(self):
        if (self.items):
            for i in self.items:
                # standard ansi colors in terminal yellow for items
                print('\x1b[1;33m' + i.name + '\x1b[1;33m')
        else:
            print('No items available')

# hello = Room()
# hello.add_item("Kili Kili Power")
# hello.get_items_list()

