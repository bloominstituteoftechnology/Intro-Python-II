from gameObj import GameObj
from color import Color

class Player(GameObj):
    def __init__(self, name, loc, desc='n/a', holding=[]):
        super().__init__(name, desc, holding)
        self.loc = loc
    
    def startGame(self):
        # DRAMATIC INTRO
        print('\n')
        self.crawlText('You awaken suddenly.')
        self.crawlText(f'Your body is aching and your clothes are stained with mud. You {Color.PURPLE}look{Color.END} around to see a locked iron gate behind you, and a gravel pathway before you. How did you get here? You touch your head and feel a lump, it is wet, and sticky. You can see a {Color.RED}Flashlight{Color.END} on the gravel nearby. It\'s YOUR flashlight.', delay=0.03)
        self.loc.getItem('flashlight', self)
        self.crawlText(f'{Color.PURPLE}It is wet with blood. Did someone knock you out with your own flashlight?{Color.END}', 0.02)
        self.crawlText(f'{Color.PURPLE}You can see your name engraved on the handle: {Color.RED}{self.name.upper()}{Color.END}', 0.02)
        self.crawlText(self.loc.desc, 0.02)

    def drop(self, thisItem):
        index = None
        for i, item in enumerate(self.holding):
            if item.name.lower() == thisItem.lower():
                index = i
        if index != None:
            thisItem = self.holding.pop(index)
            self.loc.holding.append(thisItem)
            self.crawlText(f'You dropped the {Color.RED}{thisItem.name}{Color.END}')
        else:
            print(f'You cannot see a {Color.RED}{thisItem}{Color.END}')

    def use(self, thisItem):
        index = None
        for i, item in enumerate(self.holding):
            if item.name.lower() == thisItem.lower():
                index = i
        if index != None:
            thisItem = self.holding[index]
            thisHappened = thisItem.useItem(room=self.loc.name)
            if thisItem.name == 'Flashlight':
                self.loc.isDark=False
            if thisItem.name == 'Key' and self.loc.name == 'Treasure Chamber':
                self.crawlText(f'{Color.RED}{thisHappened}{Color.END}')
                self.quitGame()
            print('\n')
            self.crawlText(f'{Color.RED}{thisHappened}{Color.END}')
        else:
            print(f'You are not holding {Color.RED}{thisItem}{Color.END}')

    def go(self, there):
        if there not in ['north','east','west','south','up','down']:
            print(f'{Color.PURPLE}{there}{Color.RED} is not an option{Color.END}')
        else:
            goTo = there[0] + '_to'
            newRoom = getattr(self.loc, goTo)
            if newRoom != None:
                self.loc = newRoom
                if self.loc.seen == False: 
                    self.loc.seen = True
                    print('\n')
                    self.crawlText(f'{Color.PURPLE}{self.loc.name}{Color.END}',0.03)
                    self.crawlText(self.loc.desc,0.02)
                else:
                    print('\n')
                    self.crawlText(f'{Color.PURPLE}You have been here before{Color.END}',0.03)
                    print(self.loc)
            else:
                print(f'{Color.RED}You cannot go {Color.PURPLE}{there}{Color.RED} from here{Color.END}')

    def __str__(self):
        return f'++ {self.name} is at the {self.loc.name} ++'
