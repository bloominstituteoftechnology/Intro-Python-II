class Foe():
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        
    def is_alive(self):
        return self.hp > 0
    
class Orc(Foe):
    def __init__(self):
        super().__init__(name='Orc', hp=20, damage=5)
        
class Goblin(Foe):
    def __init__(self):
        super().__init__(name='Goblin', hp=15, damage=3)

class Demon(Foe):
    def __init__(self):
        super().__init__(name='Demon', hp=25, damage=7)

class Monster(Foe):
    def __init__(self):
        super().__init__(name='Monster', hp=20, damage=6)
class Gremlin(Foe):
    def __init__(self):
        super().__init__(name='Gremlin', hp=10, damage=2)
