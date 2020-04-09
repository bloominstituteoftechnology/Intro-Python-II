# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None

        self.items = []

    def __str__(self):

        items_in_room = ""

        for item in self.items:
            items_in_room += f"{item}\n"

        return (
            f"{self.name}\n-----\n{self.desc}\n-----\nItems available:\n{items_in_room}"
        )

    def item_add(self, item):
        self.items.append(item)

    def item_remove(self, item):
        self.items.remove(item)
