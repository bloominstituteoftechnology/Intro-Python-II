# * Create a file called `item.py` and add an `Item` class in there.
#   * The item should have `name` and `description` attributes.
#      * Hint: the name should be one word for ease in parsing later.
#   * This will be the _base class_ for specialized item types to be declared
#     later.


class Item:
    """
    Contained in some < Room >'s,
    the player may interact with an < Item >
    to unlock mysteries throught the adventure.
    """
    name = None
    description = None

    def __init__(self, name="generic item", description="give me a description"):
        self.name = name
        self.description = description

    def __str__(self):
        return f'< Item: {self.name} >'


if __name__ == "__main__":
    print('creating new item')
    newItem = Item(
        "laptop", "it's a thankpad C29, equipped with the latest 𝝺eFTL processor.")
    print(newItem)
    print(newItem.description)
