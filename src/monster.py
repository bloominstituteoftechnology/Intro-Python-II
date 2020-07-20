class Monster:
    def __init__(self, name, base_hp=1, base_attack=0, base_defense=0, skills={}):
        self.name = name
        self.base_hp = base_hp
        self.base_attack = base_attack
        self.base_defense = base_defense
        self.skills = skills
        self.boosted_attack = 0
        self.boosted_defense = 0