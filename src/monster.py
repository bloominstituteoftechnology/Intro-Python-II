

class Monster:
    def __init__(self, name, description, hp):
        self.name = name
        self.description = description
        self.hp = hp
    def __repr__(self):
        return str(f"{self.name}")