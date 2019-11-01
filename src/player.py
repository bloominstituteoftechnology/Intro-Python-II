from gameObj import GameObj
from color import Color
from crawlText import crawlText

class Player(GameObj):
    def __init__(self, name, loc, desc='n/a', holding=[]):
        super().__init__(name, desc, holding)
        self.loc = loc

    def drop(self, thisItem):
        index = None
        for i, item in enumerate(self.holding):
            if item.name.lower() == thisItem.lower():
                index = i
        if index != None:
            thisItem = self.holding.pop(index)
            self.loc.holding.append(thisItem)
            crawlText(f'You dropped the {Color.RED}{thisItem.name}{Color.END}')
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
            print('\n')
            crawlText(f'{Color.RED}{thisHappened}{Color.END}')
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
                    crawlText(f'{Color.PURPLE}{self.loc.name}{Color.END}',0.03)
                    crawlText(self.loc.desc,0.02)
                else:
                    print('\n')
                    crawlText(f'{Color.PURPLE}You have been here before{Color.END}',0.03)
                    print(self.loc)
            else:
                print(f'{Color.RED}You cannot go {Color.PURPLE}{there}{Color.RED} from here{Color.END}')

    def __str__(self):
        return f'++ {self.name} is at the {self.loc.name} ++'
