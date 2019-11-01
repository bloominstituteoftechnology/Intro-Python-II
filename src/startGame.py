from color import Color
from crawlText import crawlText

def startGame(player):
    # DRAMATIC INTRO
    print('\n')
    crawlText(f'You awaken suddenly. Your body is aching and your clothes are stained with mud. You {Color.PURPLE}look{Color.END} around to see a locked iron gate behind you, and a gravel pathway before you. How did you get here? You touch your head and feel a lump, it is wet, and sticky. You can see a {Color.RED}Flashlight{Color.END} on the gravel nearby. It\'s YOUR flashlight.', delay=0.03)
    player.loc.getItem('flashlight', player)
    crawlText(f'{Color.PURPLE}It is wet with blood. Did someone knock you out with your own flashlight?{Color.END}', 0.02)
    crawlText(f'{Color.PURPLE}You can see your name engraved on the handle: {Color.RED}{player.name.upper()}{Color.END}', 0.02)
    crawlText(player.loc.desc, 0.02)