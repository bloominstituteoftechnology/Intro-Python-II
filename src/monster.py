class Monster:
    def __init__(self, current_room,): # hp=1, mp=1, stamina=1, Str=1, Dex=1, Con=1, Int=1, Wis=1, Cha=1):
        self.current_room = current_room
    def __str__(self):
        return str(vars(self))
