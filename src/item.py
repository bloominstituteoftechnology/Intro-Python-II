"""
BeWilder - text adventure game :: Item definition

A class to hold item information.
"""


class Item:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}: {self.description}"


class Food(Item):
    def __init__(self, name: str, description: str, calories: int):
        super().__init__(name, description)
        self.calories = calories


class Artifact(Item):
    def __init__(self, name: str, description: str, ability: str, effect: int):
        """Constructor for the base Artifact class.
        
        :param name        (str) : Name of artifact.
        :param description (str) : Description of artifact.
        :param ability     (str) : The ability that the artifact gives the player.
        :param effect      (int) : Effect which the artifact's ability has on player.
        """
        super().__init__(name, description)
        self.ability = ability
        self.effect = effect

    def __str__(self):
        return f"{self.name}: {self.description}"


class Weapon(Artifact):
    def __init__(self, name: str, description: str, ability: str, effect: int):
        """Weapon provides the player with positive offensive ability."""
        super().__init__(name, description, ability, effect)
        self.ability = "offense"


class Armor(Artifact):
    def __init__(self, name: str, description: str, ability: str, effect: int):
        """Weapon provides the player with positive defensive ability."""
        super().__init__(name, description, ability, effect)
        self.ability = "defensive"
