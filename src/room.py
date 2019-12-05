# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []
        self.hidden_items = None
        self.hidden_rooms = None
        self.is_dark = False
        self.is_locked = False

    def add_item(self, item, player):
        self.items.append(item)
        player.remove_from_inventory(item)

    def remove_item(self, item, player):
        if self.is_dark:
            print("You cannot pick up items in a dark room!")
            return
        self.items.remove(item)
        player.add_to_inventory(item)

    def view_items(self):
        if self.is_dark:
            print("You cannot see items in a dark room!")
            return

        if len(self.items) > 0:
            for item in self.items:
                print(item.name)
        else:
            print("Room contains no visible items")
