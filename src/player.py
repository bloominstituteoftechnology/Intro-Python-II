from room import Room, room
from item import Item, items


class Player:
    """
    Holds player information.
    - What room they are in currently
    - What items they are holding
    """

    def __init__(self, player_name):
        self.player_name = player_name
        self.current_room = room['outside']
        self.verb = None
        self.obj = None
        self.items = {}

    def announce(self):
        print(f'\nEntering "{self.current_room.name}"')
        print(f"Description: {self.current_room.description}\n")
        if len(self.current_room.items) > 0:
            item_name = []
            for item in self.current_room.items:
                item_name.append(item.name)
            item_names = ", ".join(item_name)
            print(f"You found {item_names} in the room.")
        else:
            print("Nothing worth taking in this room.")

    def handle_items(self, verb, obj):
        if verb in ['take', 'get', 'pick', 'grab', 'hold']:
            item_taken = 0
            for room_items in self.current_room.items:
                if obj in room_items.name:
                    item_taken += 1
                    self.items[obj.title()] = room_items.description
                    self.current_room.items.remove(room_items)
                    print(f"You {verb} the {obj} in the room.")
                    print(self.items)

            if item_taken == 0:
                print(f"There is no {obj} to pick up.")
        elif verb in ['drop']:
            if obj in self.items:
                self.current_room.items = [items[obj]]
                del self.items[obj]
                print(f"You {verb} the {obj} in the room.")
            else:
                print(f"There is no {obj} in your inventory to drop.")
        else:
            print("Something wrong with the inventory...")

    def inventory(self):
        [print(f'{k}: {v}') for k, v in self.items.items()]

    def move(self, direction):
        if direction in ["n"]:
            if self.current_room.n_to != None:
                self.current_room = self.current_room.n_to
                print("\nHeading north...")
                return self.announce()
            else:
                print("\nNo way north...")
        elif direction == "e":
            if self.current_room.e_to != None:
                print("\nHeading east...")
                self.current_room = self.current_room.e_to
                return self.announce()
            else:
                print("\nNo way east...")
        elif direction == "s":
            if self.current_room.s_to != None:
                print("\nHeading south...")
                self.current_room = self.current_room.s_to
                return self.announce()
            else:
                print("\nNo way south...")
        elif direction == "w":
            if self.current_room.w_to != None:
                print("\nHeading west...")
                self.current_room = self.current_room.w_to
                return self.announce()
            else:
                print("\nNo way west...")
