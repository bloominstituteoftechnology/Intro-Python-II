class Enemy():
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        
    def is_alive(self):
        return self.hp > 0
    
class GiantSpider(Enemy):
    def __init__(self):
        super().__init__(name="Giant Spider", hp=10, damage=2)
        
class Goblin(Enemy):
    def __init__(self):
        super().__init__(name="Goblin", hp=5, damage=1)
        

class Neutral():
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        
class Stranger(Neutral):
    def __init__(self):
        super().__init__(
            name="The Stranger",
            desc="The hollowed husk of a once famed warrior"
        )
        
neutralStranger = Stranger()
        

    