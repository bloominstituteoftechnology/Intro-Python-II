# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, entry_message, items=None):
        self.name = name,
        self.entry_message = entry_message
        if items is None:
            self.inventory = []
        else:
            self.inventory = items
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        # print(self.name, self.entry_message, self.inventory)
    def __repr__(self):
        room_string = f"{self.name[0]}\n"
        room_string += f"Narrator Message: {self.entry_message}\n"
        room_string += f"You can move: {self.get_exits()}\n"
        if len(self.inventory) > 0:
            room_string += f"You see: {self.get_items_string()}"
        return room_string 
    def get_exits(self):
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
    def get_items_string(self):
        return ", ".join([str(i) for i in self.inventory])
    def get_room_in_direction(self, direction):
        if direction == "n":
            return self.n_to
        elif direction == "e":
            return self.e_to
        elif direction == "s":
            return self.s_to
        elif direction == "w":
            return self.w_to
    def get_items_selector(self):
        return ", ".join([str(f"{i}") for i in self.inventory])
    def find_item_by_string(self, item_name):
        print(item_name)
        for index, value in enumerate(self.inventory):
            # print(value)
            if value.name == item_name:
                # print(f"{item_name} is valid, index: {index}")
                item_by_string = self.inventory[index]
                del self.inventory[index]
                # print(f"item_by_string: {item_by_string}")
                print(f"Room inventory after delete: {self.inventory}\n")
                return item_by_string
    def add_item(self, item):
        self.inventory.append(item)
        print(f"Room inventory after drop: {self.inventory}\n")










    # def room_inventory_reveal(self):
    #     return self.inventory 
    # def add_item(self, item):
    #     self.inventory.append(item)
    #     print(self.inventory)
    # def remove_item(self, item):
    #     for index, value in enumerate(self.inventory):
    #         if value.name == item.name:
    #             print(self.inventory)
    #             print(value)
    #             print(index)
    #             # del(self.inventory[index])

