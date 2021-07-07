class Item:
    """
    The Item class have name and description attributes.

    Hint: the name should be one word for ease in parsing later.
    This will be the base class for specialized item types to be declared later.
    """

    def __init__(self, name, description):
        self.name = name
        self.description = description


# Declare all items
items = {
    'hammer': Item("hammer", "Good for smashing"),

    'tablet': Item("tablet", """Duo screen tablet with unlimited data"""),

    'candle': Item("candle", """Good for burning""")
}
