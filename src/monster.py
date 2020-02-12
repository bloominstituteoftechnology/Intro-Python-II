class Monster:
    def __init__(self, name, description, hp, damage):
        self.name = name
        self.description = description
        self.hp = hp
        self.damage = damage

    def on_attack(self, weapon):
        self.hp = self.hp - weapon.damage
        print(f"You swing your {weapon.name} at the {self.name}. You do {weapon.damage} damage.")
        print(f"The monster has {self.hp} hp remaining.\n")
