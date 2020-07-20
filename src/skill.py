class Skill:
    def __init__(self, name, damage, skill_type, effect=None):
        self.name = name
        self.damage = damage
        self.skill_type = skill_type
        self.effect = effect
    def __str__(self):
        return self.name
    def on_skill_call(self):
        return f"used {self.name}"