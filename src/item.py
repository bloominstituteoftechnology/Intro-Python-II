class Item(object):
    """A game item.

    :var name: str - name of Item
    :var description: str - description of Item
    :var weight: int - default 0

    """

    def __init__(self, name: str, description: str, weight: int = 0) -> None:
        self.name = name
        self.description = description
        self.is_light = False
        self.weight = weight
        self.active = False
        # TODO: Add 'seen' functionality

    def __str__(self) -> str:
        return f"{self.name}, {self.description}"

    def __repr__(self) -> str:
        return self.description

    def on_get(self) -> None:
        """Print statement confirming item added to inventory."""
        print(f"I have added the {self.name} to the inventory. \n")

    def on_drop(self) -> None:
        """Print statement confirming item added to inventory."""
        print(f"I have dropped the {self.name}")


class Container(Item):
    """An Item that holds Items.

    Inherits from Item

    """

    def __init__(self, name: str, description: str, weight: int = 0) -> None:
        super().__init__(name, description, weight)
        self.locked = False
        self.key = None
        self.items_ = {}


class Weapon(Item):
    """An attack Item.

    Inherits from Item

    """

    def __init__(self, name, description, weight, attack) -> None:
        super().__init__(name, description, weight)
        self.attack = attack


class Shield(Item):
    """A shielding Item.

    Inherits from Item

    """

    def __init__(self, name, description, weight, shield) -> None:
        super().__init__(name, description, weight)
        self.shield = shield
