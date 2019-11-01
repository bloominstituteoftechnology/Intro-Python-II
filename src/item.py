from player import Player


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
        self.seen = False

    def __str__(self) -> str:
        return f"{self.name}, {self.description}"

    def __repr__(self) -> str:
        return self.description

    def on_get(self, *args) -> None:
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


class SlingShot(Item):
    """An attack Item.

    Inherits from Item

    """

    def __init__(self, name: str, description: str, weight: int, owner: Player = None) -> None:
        super().__init__(name, description, weight)
        self.owner = owner

    def shoot(self, character: Player) -> None:
        """Increase character attackpts to reflect use of sling shot.

        calls owner._attack() then decreases attackpts to baseline.
        :var character: The character to attack
        """
        self.owner.attackpts += 30
        self.owner._attack(character)
        self.owner.attackpts -= 30

    def on_get(self, player: Player = None) -> None:
        """Update self to have an owner and the owner to have a sling shot.

        :var player: The proud owner of a new slingshot
        """
        self.owner = player
        self.owner.has_slingshot = True
        super().on_get()
        if not self.owner.has_pebbles:
            print("Sweet! Now I need some ammo! \n")

    def blank(self):
        """Nothing to shoot at or no ammo."""
        if not self.owner.has_pebbles:
            print("You need some ammo first. \n")
        else:
            print("There's nothing to shoot. Better conserve ammo.\n")


class Pebbles(Item):
    """A rock Item.

    Inherits from Item

    """

    def __init__(self, name: str, description: str, weight: int, owner: Player = None) -> None:
        super().__init__(name, description, weight)
        self.owner = owner

    def on_get(self, player: Player = None) -> None:
        """Update self to have an owner and owner to have pebbles.

        :var player: The proud owner of new pebbles.
        """
        self.owner = player
        self.owner.has_pebbles = True
        super().on_get()

    def rock(self):
        """Be rock."""
        print("I'm just a rock.")


class Berries(Item):
    """Delicious Berries.

    Restore 15 hp by eating.

    """

    def __init__(self, name: str, description: str, weight: int = 3) -> None:
        super().__init__(name, description, weight)
        self.owner = None

    def on_get(self, player: Player = None) -> None:
        """Update self to have an owner and owner to have berries.

        :var player: The proud owner of new berries.
        """
        self.owner = player
        super().on_get()

    def eat(self):
        """Consume berries, feel better."""
        old = self.owner.hp
        self.owner.hp += 15
        self.owner.items_.pop(self.name, None)
        print(f"{self.owner.name} health has gone from {old} to {self.owner.hp} \n")
