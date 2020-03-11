
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

    def __repr__(self):
        return self.name
        


class Generic(Item):
    """A class for generic items"""
    def __init__(self):
        self.attrib = ''

class Weapon(Item):
    def __init__(self, ID,
                name='MissingNo',
                description='Definitely not a bug...',
                damage=0,
                reach=0,
                dmg_type=Generic
                ):
        super().__init__(ID, name=name, description=description)
        self.damage = damage
        self.reach = reach
        self.dmg_type = dmg_type