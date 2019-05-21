class Monster:
    
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def its_alive(self):
        return self.hp > 0


class ZombieSkeleton(Monster):
    def __init__(self):
        super().__init__(name="Zombie Skeleton", hp=20, damage=10)


class GiantWorm(Monster):
    def __init__(self):
        super().__init__(name="Giant Worm", hp=25, damage=15)
