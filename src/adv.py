from room import Room
from player import Player
from item import Item, LightSource
import re

# Declare all the rooms
'''
Items and their descriptions are taken from the 
https://www.google.com/search?q=morriwind+game+items&rlz=1C5CHFA_enUS729US729&oq=morriwind+game+items&aqs=chrome..69i57.13182j1j8&sourceid=chrome&ie=UTF-8
website. (Morrowind | Elder Scrolls)
'''
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     [Item("Helm", "Bloodworm Helm is a unique heavy enchanted Nordic Trollbone Helm. This item can be sold at the Museum of ArtifactsTR for 17,000 GoldIcon.")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
                     [Item("Boots", "The Boots of Blinding Speed are a unique set of Netch Leather Boots found in The Elder Scrolls III: Morrowind. Their effectiveness is determined by the character's skill level in the Light Armor skill."),
                      LightSource("Lamp", "A Bug Lamp is a miscellaneous item in The Elder Scrolls III: Morrowind. This item provides a portable light source which can be carried in the left hand while traveling.")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("Locket", "Hlervu Locket is an unique amulet in The Elder Scrolls III: Morrowind. It is a prized possession of the family of Braynas Hlervu, but was taken from him when he could not pay his taxes. During the quest 'The Hlervu Locket', it must be stolen from within Venim Manor and given back to his owner.")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item("Sword", "Sword of Agustas is a unique enchanted Nordic claymore that belonged to Agustas. It can be found next to his remains in the northwest room of the Arenim Ancestral Tomb.")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['outside'].n_to = room['foyer']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

def game():
    # player_name = input(f"\n What is your name? \n Enter Your Name : ")
    player = Player(current_room = room["outside"])

    print(" ")
    print("Welcome to the ADVENTURE Game!")
    answer = input("Are you ready for an adventure? Y/N ").lower().strip()
    print(" ")

    if answer == "y":
        playing = True
        player.describe_room()

        while playing == True:

            player_answer = input("\nWhat's your next move? \nGo North [n] South [s] East [e] West [w] \nCheck for items in the room [look] \nCheck if the Light is On [light]\nCheck your Inventory [i] \n· Get Item [get 'item'] · Drop Item [drop 'item'] \nQuit [q]")
            answer = tokenizer(player_answer)

            if len(answer) == 1:
                if answer[0][1] in ["n", "s", "e", "w"]:
                    if player.move_player(answer[0][1]) == True:
                        player.describe_room()
                    else:
                        print("\n   There is no way to go that direction.  \n")
                elif answer[0][1] == "l" or answer[0][1] == "look":
                    player.current_room.look_around()
                elif answer[0][1] == "i":
                    player.check_inventory()
                elif answer[0][1] == "light":
                    player.is_light_on()
                elif answer[0][1] == "q":
                    playing = False
                else:
                    print("\n  That action is not available.  \n")

            elif len(answer) == 3:
                if answer[0][1]== "get":
                    a = 0
                    for i in player.current_room.inventory:
                        if i.name == answer[2][1] or i.name == (answer[2][1]).capitalize():
                            a +=1
                            player.current_room.remove_item(i)
                            player.pick_item(i)
                            if i.name == Lamp.name:
                                i.light_on = True
                    if a == 0:
                        print("\n The item isn't in this room. \n")
                elif answer[0][1] == "drop":
                    if len(player.inventory) == 0:
                        print("\n You currently don't have any items. \n")
                    a = 0
                    for i in player.inventory:
                        if i.name == answer[2][1] or i.name == (answer[2][1]).capitalize():
                            a += 1
                            if i.name == Lamp.name:
                                i.light_on = False
                                print("\n It's not wise to drop your source of light!")
                            player.drop_item(i)
                            player.current_room.add_item(i)
                    if a == 0:
                        print(f"\n You don't have a {answer[2][1]}. \n")

                else:
                    print("\n  That action is not available.  \n")
            
            else:
                    print("\n  That action is not available.  \n")


    else:
        print("\n  Oh well, see you later!")
        return


tokens = (
  ('STRING', re.compile('"[^"]+"')),  # longest match
  ('ID', re.compile('[a-zA-Z_]+')),
  ('SPACE', re.compile('\s+')),
  ('DIGIT', re.compile('\d+')),
)

def tokenizer(s):
  i = 0
  lexeme = []
  while i < len(s):
    match = False
    for token, regex in tokens:
      result = regex.match(s, i)
      if result:
        lexeme.append((token, result.group(0)))
        i = result.end()
        match = True
        break
    if not match:
      raise Exception('lexical error at {0}'.format(i))
  return lexeme

Lamp = LightSource("Lamp", "A Bug Lamp is a miscellaneous item in The Elder Scrolls III: Morrowind. This item provides a portable light source which can be carried in the left hand while traveling.")

game()
