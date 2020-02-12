from random import random
from lightsource import Lightsource


class Room:
    def __init__(self, name, description, items, light, has_unique_action=False, enemies=[],):
        self.name = name
        self.description = description
        self.items = items
        self.light = light
        self.enemies = enemies
        self.has_unique_action = has_unique_action
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def check_light(self, player):
        for i in player.items:
            if isinstance(i, Lightsource):
                self.light = True

    def run_room_action(self, room_key, player, action):
        """If a room has some unique actions attached to it,
        allow the player to perform these actions."""
        if room_key == 'overlook':
            if len(action) > 1 and 'rope' in action:
                print("""You hurl the rope across the chasm in a desperate attempt to
form a makeshift bridge. Miraculously, it fastens itself around a 
tree stump, winding around several times before being trapped between
two boulders. You test it - it seems sturdy.\n""")
                sub_action = input(
                "Do you want to try and cross the chasm?\n").strip().split()
                if 'yes' in sub_action or 'cross' in sub_action:
                    if random() < 0.99:
                        print("""You grit your teeth and curse your crippling addiction to treasure
hunting. Heart pounding, you grip the rope and start to shimmy across.
At one point you could swear you feel it start to slip, and you wonder if 
this is it - but then suddenly your head knocks against the opposite side
of the cliff. You scramble up - you've made it.\n""")
                        player.points += 10
                        print(f"You have {player.points} points.")
                        player.move('n')
                        for i in player.items:
                            if i.name == 'rope':
                                player.items.remove(i)
                    else:
                        print("""You leap forth heroically and grab the rope in both hands. It immediately
dislodges and you fall screaming to your immediate death into a shallow river full of spiky rocks.
Oh well, you can always try again....\n""")
                        exit()

        if room_key == 'dark':
            if 'read' in action:
                print(
                    "You take your lamp in one hand and squint at the note. You can make out some text\n")
                print(
                    "1T'S A TR4P! DON'T G0 THROUGH THE SECRET DOOR IN EAST SIDE OF THE TREASURE ROOM!\n")
                for i in player.current_room.items:
                    if i.name == 'note':
                        player.items.append(i)
                        player.current_room.items.remove(i)

        if room_key == 'treasure':
            for i in player.items:
                if i.name == 'note':
                    print("""Looking closely at the east side of the room, you can see a faint outline among
the rocks. Brushing the dust away, you see the outline of a dusty, stone-coloured door. In the centre
is a keypad and a screen. You're puzzled by this sudden thematic inconsistency with the fantasy theme 
that this game has so far maintained.""")
            sub_action = input("What do you do?").strip().split()
            if 'enter' in sub_action or 'type' in sub_action:
                if sub_action[1] == '140':
                    print("The door swings open!")
                    player.move('n')
                else:
                    print("Nothing happens.")