# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, is_light):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.is_light = is_light
        self.light_source = None
        self.items = []

    def __repr__(self):
        returnString = f"---------------\n\n{self.name}\n\n  {self.description}\n\n---------------"
        returnString += f"\n\n[{self.getRoomExitString()}]\n\n"
        return returnString

    def all_room_items(self):
        my_items = []
        for item in self.items:
            my_items.append(item.name)
        return my_items

    def getRoomInDirection(self, direction):
        if direction == "n":
            return self.n_to
        elif direction == "s":
            return self.s_to
        elif direction == "w":
            return self.w_to
        elif direction == "e":
            return self.e_to
        else:
            return None

    def getRoomExitString(self):
        exits = []
        if self.n_to is not None:
            exits.append("n")
        if self.s_to is not None:
            exits.append("s")
        if self.e_to is not None:
            exits.append("e")
        if self.w_to is not None:
            exits.append("w")
        return ", ".join(exits)

    def remove_item(self, item):
        self.items.remove(item)
        print(f"{self.name} now has: {self.all_room_items()}")
