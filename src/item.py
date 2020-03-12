
class Item:
    """Base class for Items.
    You should not instantiate this class alone

    Keyword Arguments:
    name {str} -- [Name of item] (default: {'MissingNo'})
    description {str} -- [Description of room, get creative!] (default: {'Definitely not a bug...'})
    type {Class} -- [Class of item. ie: Weapon, Gear, Food, Key, etc] (default: {Generic})
    """
    def __init__(self, ID, name='MissingNo', description='Definitely not a bug...',):
        self.ID = ID
        self.name = name
        self.description = description

    def on_take(self):
        print(f'You picked up {self.name}')
    
    def on_drop(self):
        print(f'You dropped {self.name}')

    def __repr__(self):
        return self.name

class Generic(Item):
    """A temp class for non weapon items"""
    def __init__(self):
        self.attrib = ''

class Weapon(Item):
    def __init__(self, ID, name, description,
                damage=0,
                reach=0,
                dmg_type=''
                ):
        super().__init__(ID, name=name, description=description)
        self.damage = damage
        self.reach = reach
        self.dmg_type = dmg_type


class Sword(Weapon):
    def __init__(self, ID):
        super().__init__(ID, 'sword', "A simple bladed weapon", 
            damage=5, reach=None, dmg_type='slashing')



class LightSource(Item):
    def __init__(self, ID, name, description,
                intensity):
        super().__init__(ID, name=name, description=description)
        self.intensity = intensity

class Lantern(LightSource):
    def __init__(self, ID,):
        super().__init__(ID, 'lantern', 'A simple oil lantern', 'high')

class Food(Item):
    def __init__(self, name, description, calories):
        super().__init__(name, description)
        self.calories = calories


