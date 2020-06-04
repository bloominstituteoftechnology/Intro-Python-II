class RandWeapon:
    def __init__(self, weaponPrefix, weaponSuffix, weaponType):
        self.weaponPrefix = weaponPrefix
        self.weaponSuffix = weaponSuffix
        self.weaponType = weaponType

    def getweaponPrefix(self):
        return self.weaponPrefix[random.randint(0, len(self.weaponPrefix) - 1)]

    def getweaponSuffix(self):
        return self.weaponSuffix[random.randint(0, len(self.weaponSuffix) - 1)]
 
    def getweaponType(self):
        return self.weaponType[random.randint(0, len(self.weaponType) - 1)]

    def get_weapon(self):
        return '{} {}'.format(self.getRandomStats(), self.getRandomTypes())


weaponPrefix = ['silver', 'ornate', 'broken', 'superior', 'keen', 'savage', 'light', 'heavy', 'dull', 'sharp', 'massive', 'forgotten']
weaponSuffix = ['of the bear', 'of the eagle', 'of the boar', 'of the moongoose', 'of the damned']
weaponTypes = ['katar', 'stiletto', 'dirk', 'shortsword', 'claymore', 'falchion', 'sabre', 'quarterstaff', 'maul', 'mace', 'flail', 'club', 'bow', 'crossbow', 'sling', 'bardiche', 'halberd', 'lance', 'pike', 'sovnya', 'voulge']
weaponRare = ["the void star", "urn the siege breaker", "arborath the foe hammer"]
rw = RandWeapon(weaponStats, weaponTypes)