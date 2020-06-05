import random

class RandWeapon:

    def __init__(self, weaponMaterial, weaponPrefix, weaponTypes):
        self.weaponMaterial = weaponMaterial
        self.weaponPrefix = weaponPrefix
        self.weaponTypes = weaponTypes

    def getRandomMaterial(self):
        return self.weaponMaterial[random.randint(0, len(self.weaponMaterial) - 1)]

    def getRandomPrefix(self):
        return self.weaponPrefix[random.randint(0, len(self.weaponPrefix) - 1)]
 
    def getRandomTypes(self):
        return self.weaponTypes[random.randint(0, len(self.weaponTypes) - 1)]

    def get_weapon(self):
        return '{} {} {}'.format(self.getRandomPrefix(),
                                 self.getRandomMaterial(),
                                 self.getRandomTypes())
    
    def __str__(self):
        return "{} {} {}".format(self.getRandomPrefix(),
                                 self.getRandomMaterial(),
                                 self.getRandomTypes())    

### Prefix ####
weaponPrefixShared = [
    "Ornate", "Broken", "Superior", "Heavy", "Light", "Massive", "Strange",
    "Common", "Blessed", "Strong", "Sturdy"
    ]
weaponPrefixRange = [
    "Refined", "Reinforced", "Deformed", "Rotten", "Accurate", "Laminated"
    ]
weaponPrefixMelee = [
    "Dull", "Sharp", "Massive"
    ]

### Materials ###
weaponMaterialShared = []
weaponMaterialRange = [
    "Yew", "Maple", "Wych Elm", "Ash", "Hawthorn", "Apple", "Pear", "Cherry", "Laburnum",
    "Birch", "Hackberry", "Hornbeam", "Ipe", "Juniper", "Lemonwood", "Oak", "Mulberry",
    "Witch Hazel", "Walnut", "Teak", "Snakewood"
    ]
weaponMaterialMelee = [
    "Bronze", "Copper", "Iron", "Steel", "Ivory", "Silver", "Brass"
    ]

### Weapons ###
weaponMeleeStarter = [
    "Sword", "Claymore", "Shortsword", "Longsword", "Greatsword", "Saber"
    ]
weaponRangeStarter = [
    "Bow", "Longbow", "Shortbow", "Recurve Bow", "Siege Bow", "Hunter's Bow", "Flatbow"
    ]

##### Master List #####
weaponMasterPrefixMelee = weaponPrefixShared + weaponPrefixMelee
weaponMasterPrefixRange = weaponPrefixShared + weaponPrefixRange
weaponMasterMaterialMelee = weaponMaterialShared + weaponMaterialMelee
weaponMasterMaterialRange = weaponMaterialShared + weaponMaterialRange

# starterSword01 = RandWeapon(weaponMasterMaterialMelee, weaponMasterPrefixMelee, weaponMeleeStarter)
# starterBow01 = RandWeapon(weaponMasterMaterialRange, weaponMasterPrefixRange, weaponRangeStarter)

    
# starterBow.get_weapon()
# starterSword.get_weapon()

# print(starterSword)
# print(starterBow)

# weaponPrefix = ['silver', 'ornate', 'broken', 'superior', 'keen', 'savage', 'light', 'heavy', 'dull', 'sharp', 'massive', 'forgotten']
# weaponSuffix = ['of the bear', 'of the eagle', 'of the boar', 'of the moongoose', 'of the damned']
# weaponTypes = ['katar', 'stiletto', 'dirk', 'shortsword', 'claymore', 'falchion', 'sabre', 'quarterstaff', 'maul', 'mace', 'flail', 'club', 'bow', 'crossbow', 'sling', 'bardiche', 'halberd', 'lance', 'pike', 'sovnya', 'voulge']
# weaponRare = ["the void star", "urn the siege breaker", "arborath the foe hammer"]
# # rw = RandWeapon(weaponStats, weaponTypes)

# starterSword = RandWeapon(weaponPrefix, weaponType)
# starterSword.get_weapon()

if __name__ == "__main__":
    print('\n'*2)
    print(f'<<< Starter Weapon (Melee) Test >>>')
    def RandMeleeTEST():
        num = 1
        while num <= 100:
            starterSwordTEST = RandWeapon(weaponMasterMaterialMelee, weaponMasterPrefixMelee, weaponMeleeStarter)
            print(starterSwordTEST)
            num += 1    
    
    RandMeleeTEST()
    print('\n'*2)
    print(f'<<< Starter Weapon (Range) Test >>>')
    def RandRangeTEST():
        num = 1
        while num <= 100:
            starterRANGETEST = RandWeapon(weaponMasterMaterialRange, weaponMasterPrefixRange, weaponRangeStarter)
            print(starterRANGETEST)
            num += 1

    RandRangeTEST()
    