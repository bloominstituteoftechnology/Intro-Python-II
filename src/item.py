class Item:
    """Base class for Items"""
    def __init__ (self, name, description):
        self.name = name
        self.description = description

    def on_take (self):
        print(f'You have picked up {self.name}')
    
    def on_drop (self):
        print(f'You dropped {self.name}')

    def __repr__ (self):
        return self.name

class Coin(Item):
    def __init__ (self):
        super().__init__(name='coin', description='use the key to enter in the cave')        

class LightSource(Item):
    def __init__ (self):
        super().__init__(name=name, description=description)

class Lamp(LightSource):
    def __init__ (self):
        super().__init__(name='lamp', description='a candle lamp')     

class Weapon(Item):
    def __init__ (self):
        super().__init__(name=name, description=description)  

class Sword(Weapon):
    def __init__ (self):
        super().__init__(name=name, description=description)

class Knife(Weapon):
    def __init__ (self):
        super().__init__(name=name, description=description)          

class Poison(Weapon):
    def __init__ (self):
        super().__init__(name=name, description=description) 

class MagicPotion(Weapon):
    def __init__ (self):
        super().__init__(name=name, description=description)                         

class Food(Item):
    def __init__ (self):
        super().__init__(name=name, description=description) 

class PoisonedFood(Food):
    def __init__ (self):
        super().__init__(name=name, description=description)  

class PoisonedWine(Food):
    def __init__ (self):
        super().__init__(name=name, description=description)          

class Treasures (Item):
    def __init__ (self):
        super().__init__(name=name, description=description)                            



        


