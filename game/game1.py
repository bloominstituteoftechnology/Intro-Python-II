"""

You are a pirate and have found a treasure map. Treasure is well hidden, and any wrong move you take will lead to your demise.
Can you reach the treasure.

"""

class Islands:
    def __init__(self):
        self.levels = [range(4)]
        self.space =  6  # round(levels[n]*2)
        self.islands = ['foo','bar','Caribbean','Storm']
        self.location_dict = dict(zip(range(1,5), self.islands))
        

    def move_to_island(self, navigation=[]):
        self.navigation = [s for s in input('Hey there, please select where you would like to go (acceptable moves n,w,e,s): ')]
        # self.n = n
        # self.s = s
        # self.w = w
        # self.e = e

        for l in self.navigation:
              if l not in ['n','s','w','e']:
                      while True:
                          try:
                              # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
                              self.navigation = [s for s in input(f"Hey there, this is not 2010, we only travel in normal dimensions \n you can only move n, s, e, w \n change that {l}: \n")]
                          except ValueError:
                              print("No comprendo but in 2010 language")
                              #better try again... Return to the start of the loop
                              continue
                          else:
                              #age was successfully parsed!
                              #we're ready to exit the loop.
                              break

        self.n = self.navigation.count('n')
        self.s = self.navigation.count('s')
        self.w = self.navigation.count('w')
        self.e = self.navigation.count('e')

        total_count = self.n+self.s+self.e+self.w

        if total_count >= 5:
            self.island = 'end of the world'
        else:
            self.island = i.location_dict[total_count]

        # location_dict = dict(zip(islands,range(4)))

    def __str__(self):

        if self.island == 'Storm':
            i = 'You just sailed into the storm and met your demise'

        elif self.n+self.s+self.e+self.w >= 5:
            i = f'You just hit a wall, it appears you reached the {self.island}.'

        else:
            i = f'You just reached the {self.island} island'
        
        return i

class Items:
    def __init__(self, name, power, can_hold):
        self.name = name
        self.power = power
        self.can_hold = can_hold
        # self.items = ['Ship', 'Key', 'Chest', 'Hammer', 'Food']

    def list_items(self):
        return self.items

class Weapons(Items):
        def __init__(self, name, power, can_hold, energy=3):
                super().__init__(name, power, can_hold)
                self.energy = energy

class Transportation(Items):
        def __init__(self, name, power, can_hold, health=10):
                super().__init__(name, power)
                self.can_hold = False
                self.health = health

class Healing(Items):
        pass


class Bag:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        if item not in it.list_items():
            print(f'{item} not in items')
        else: 
            self.items.append(item)

    def __str__(self):
        b = f'Items: \n'

        for n, it in enumerate(self.items, start=1):
            b +=  f' {n}. {it}'
        
        return b


i = Islands()

b = Bag()
it = Items()

b.add_item('Ship')
b.add_item('x')

i.move_to_island()

print(i)
print(b)
