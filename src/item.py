from room import Room


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{name} {description}"

    def grab_item(self):
        pass

    def drop_item(self):
        pass


class Weapon(Item, Room):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.power = name
        self.grabbed = False
