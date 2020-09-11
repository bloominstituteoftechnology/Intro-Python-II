# Implement a class to hold room information. This should have name and
# description attributes.

# * Add the ability to add items to rooms.

#   * The `Room` class should be extended with a `list` that holds the `Item`s
#     that are currently in that room.

#   * Add functionality to the main loop that prints out all the items that are
#     visible to the player when they are in that room.

class Room:

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.list = []

    def __str__(self):
        output = "\n"
        output += f"room name: {self.name}\n"
        output += f"room description: {self.description}\n"
        if len(self.list):
            output += f"room has the following items:\n"

        for idx, item in enumerate(self.list):
            output += f"{idx+1}. item name: {item.name}\n   item desc: {item.description}\n"
        output += "\nExits to the: "
        output += f"\n[North] {self.n_to.name}" if hasattr(
            self, "n_to") else ""
        output += f"\n[South] {self.s_to.name}" if hasattr(
            self, "s_to") else ""
        output += f"\n[East] {self.e_to.name}" if hasattr(self, "e_to") else ""
        output += f"\n[West] {self.w_to.name}" if hasattr(self, "w_to") else ""
        return output

    def append_item(self, item):
        self.list.append(item)
        print(f'Item {item.name} added to {self.name}\n')
