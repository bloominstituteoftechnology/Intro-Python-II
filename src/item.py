"""
BeWilder - text adventure game :: Item definition

A class to hold item information.
"""


class Item:
    def __init__(self, name: str, description: str):
        """Base class for more specialized items.
        
        :param name (str) : Name of the item.
        :param description (str) : Short description of the item.
        """
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}: {self.description}"


class Consumable(Item):
    def __init__(self, name: str, description: str, effect: int):
        super().__init__(name, description)
        self.effect = effect

    def consume(self):
        pass


class Food(Consumable):
    def __init__(self, name: str, description: str, effect: int):
        super().__init__(name, description, effect)


class Medicine(Consumable):
    def __init__(self, name: str, description: str, effect: int):
        """Medicine's effect is increased hp when consumed.
        
        :param Consumable (Item) : Parent class, which is child of Item.
        :param effect (int) : Number of hp gained when consumed.
        """
        super().__init__(name, description, effect)


class Artifact(Item):
    def __init__(
        self,
        name: str,
        description: str,
        ability: str,
        effect: int,
        requires: str = None,
    ):
        """Constructor for the base Artifact class.
        
        :param ability     (str) : The ability provided by obtaining the artifact.
        :param effect      (int) : Effect which the artifact's ability has on player.
        :param requires    (str) : Additional artefact required to use the artefact. 
        """
        super().__init__(name, description)
        self.ability = ability
        self.effect = effect
        self.requires = requires

    def __str__(self):
        return f"{self.name}: {self.description}"


class Weapon(Artifact):
    def __init__(
        self, name: str, description: str, effect: int, requires: str = None,
    ):
        """Weapon provides the player with positive offensive ability."""
        super().__init__(name, description, effect, requires)
        self.ability = "offense"


class Armor(Artifact):
    def __init__(
        self, name: str, description: str, effect: int, requires: str = None,
    ):
        """Weapon provides the player with positive defensive ability."""
        super().__init__(name, description, effect, requires)
        self.ability = "defensive"

