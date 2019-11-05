from gameObj import GameObj
from color import Color

class Room(GameObj):
    def __init__(self, name, desc, holding=[], isDark=False):
        super().__init__(name, desc, holding, isDark)
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.u_to = None
        self.d_to = None

    def getItem(self, thisItem, player):
        index = None
        for i, item in enumerate(self.holding):
            if item.name.lower() == thisItem.lower():
                index = i
        if index != None:
            thisItem = self.holding.pop(index)
            player.holding.append(thisItem)
            if thisItem.name == 'Rubber Duck':
                self.crawlText(f'You pick up the {Color.RED}{thisItem.name}{Color.END}')
                self.crawlText(f'{Color.PURPLE}{thisItem.desc}{Color.END}', 0.03)
                self.crawlText(f'{Color.RED}You hear a faint growl growing louder. As you turn to {Color.PURPLE}look{Color.RED}, the growl explodes into a bark. You can see death in the eye of the beast. You hear nothing as you fall to the ground, the weight of a giant dog pressing you into the mud. The pain is terrible, and you faintly remember two words from a past life: {Color.PURPLE}King Corso.{Color.END}', 0.03)
                self.quitGame()
            else:
                self.crawlText(f'You pick up the {Color.RED}{thisItem.name}{Color.END}')
                if thisItem.seen == False:
                    thisItem.seen = True
                    self.crawlText(f'{Color.PURPLE}{thisItem.desc}{Color.END}', 0.03)
                else:
                    print(f'{Color.PURPLE}{thisItem.desc}{Color.END}')
        elif index == None:
            print(f'You cannot see a {Color.RED}{thisItem}{Color.END}')

    def __str__(self):
        return f'{self.desc}\n'