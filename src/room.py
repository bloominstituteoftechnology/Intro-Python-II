# Implement a class to hold room information. This should have name and
# description attributes.

# * Add the ability to add items to rooms.
#   * The `Room` class should be extended with a `list` that holds the `Item`s
#     that are currently in that room.
#   * Add functionality to the main loop that prints out all the items that are
#     visible to the player when they are in that room.
# * Add capability to add `Item`s to the player's inventory. The inventory can
#   also be a `list` of items "in" the player, similar to how `Item`s can be in a
#   `Room`.


class Room:
    """
    < Room > is traveled by < Player >
    """
    name = None
    description = None
    items = None

    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items

    def __str__(self):
        return f'<Room: {self.name}>'

    def available(self, itemName):
        """
        available < Item >(s) named [itemName]
        """
        return len(list(filter(lambda x: x.name.lower() == itemName.lower(), self.items)))

    def takeItem(self, name):
        """
        take < Item > from room by [name]
        """
        # filter by name
        i = list(filter(lambda x: x.name == name, self.items))
        if not len(i) > 0:
            # if no matches,
            return False
        # if we have a match, find the index number
        idx = self.items.index(i[0])
        # remove it from available items
        removed = self.items.pop(idx)
        return removed

    def dropItem(self, item):
        """
        drop < Item > in this room
        """
        self.items.append(item)


if __name__ == "__main__":
    print('creating new Room')
    room = Room("LambdaSchool", "a place for learning how to learn")
    print(room)
