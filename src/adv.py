from room import Room
from player import Player

# All the rooms

room = {
    'winterfell':   Room("Winterfell", "Winterfell is the seat and the ancestral home of the royal House Stark. It is a very large castle located at the center of the North, from where the head of House Stark rules over his or her people.", "🐺"),

    'riverrun':    Room("Riverrun", "Riverrun is the seat of House Tully, which was once occupied by House Frey. It is a large castle located in the central-western part of the Riverlands.", "⛲️"),

    'kings_landing': Room("Kings Landing", "King's Landing is the capital, and largest city, of the Seven Kingdoms. It enjoys a warm climate and life there is luxurious for those that can afford it.", "👑"),

    'eyrie':   Room("Eyrie", "The Eyrie is the principal stronghold of House Arryn. It is located in the Vale of Arryn near the east coast of Westeros. ", "🗻"),

    'casterly_rock': Room("Casterly Rock", "Casterly Rock is the ancestral stronghold of House Lannister. It is located on the Western coast of Westeros on a rocky promontory overlooking the Sunset Sea.", "👫"),

    'pyke': Room("Pyke", "Pyke is the stronghold and seat of House Greyjoy, located on the island of the same name, which is one of the seven major Iron Islands. ", "⚓️"),

    'highgarden': Room("Highgarden", "Highgarden was the seat of House Tyrell and is the regional capital of the Reach. Located on the banks of the river Mander, Highgarden sits astride the Roseroad, a major thoroughfare linking Oldtown and King's Landing.", "🏆"),

    'stormsend': Room("Storm's End", "Storm's End is the ancestral seat of House Baratheon. Lord Gendry Baratheon is the Lord of Storm's End. Storm's End is a formidable fortress, located on the southeastern coast of Westeros overlooking Shipbreaker Bay.", " 🌊"),

    'sunspear': Room("Sunspear", "Sunspear is the capital of Dorne Dorne, southernmost of the Seven Kingdoms, located in the far southeast of the continent on the Summer Sea.", "☀️")
}

# Player
player = Player("Ivana", room["winterfell"])

# Link rooms together
room['winterfell'].n_to = room['riverrun']

room['pyke'].n_to = room['casterly_rock']
room['pyke'].e_to = room['riverrun']

room['riverrun'].n_to = room['highgarden']
room['riverrun'].s_to = room['winterfell']
room['riverrun'].w_to = room['pyke']
room['riverrun'].e_to = room['eyrie']

room['eyrie'].w_to = room['riverrun']
room['eyrie'].n_to = room['kings_landing']


room['casterly_rock'].s_to = room['pyke']
room['casterly_rock'].e_to = room['highgarden']

room['highgarden'].w_to = room['casterly_rock']
room['highgarden'].e_to = room['kings_landing']
room['highgarden'].s_to = room['riverrun']
room['highgarden'].n_to = room['sunspear']

room['kings_landing'].s_to = room['eyrie']
room['kings_landing'].n_to = room['stormsend']
room['kings_landing'].w_to = room['highgarden']

room['sunspear'].s_to = room['highgarden']
room['sunspear'].e_to = room['stormsend']

room['stormsend'].w_to = room['sunspear']
room['stormsend'].s_to = room['kings_landing']

# Messages
hello = f"\n==========================================================\n 🌏   Hello and welcome to TRAVEL AROUND WESTEROS\n==========================================================\n"
goodbye = f"\n==========================================================\n                   THANK YU FOR PLAYING!\n==========================================================\n"
where_to_go = f"❔   Would you like to stay or go somewhere else? Use n/s/w/e for navigation: "
walking = "walking ..."


# Game logic
directions = ''

print(f"{hello}")
print(
    f"{player.name} You are currently in {player.current_room.name.upper()} {player.current_room.emoji} ")

while directions != 'q':
    directions = input(f"{where_to_go}")
    try:
        if directions == "n":
            if player.current_room.s_to:
                player.current_room = player.current_room.s_to
                print(f"{walking}")
                print(
                    f"You have decided to go north and you moved to {player.current_room.name.upper()} {player.current_room.emoji}")
                print(f"{player.current_room.describtion}")
            else:
                print(
                    f"⬆️  There is nothing north of {player.current_room.name.upper()} {player.current_room.emoji}")
        elif directions == "s":
            if player.current_room.n_to:
                player.current_room = player.current_room.n_to
                print(f"{walking}")
                print(
                    f"You have decided to go south and you moved to {player.current_room.name.upper()} {player.current_room.emoji}")
                print(f"{player.current_room.describtion}")
            else:
                print(
                    f"⬇️  There is nothing south of {player.current_room.name.upper()} {player.current_room.emoji}")
        elif directions == "e":
            if player.current_room.w_to:
                player.current_room = player.current_room.w_to
                print(f"{walking}")
                print(
                    f"You have decided to go east and you moved to {player.current_room.name.upper()} {player.current_room.emoji}")
                print(f"{player.current_room.describtion}")
            else:
                print(
                    f"➡️  There is nothing east of {player.current_room.name.upper()} {player.current_room.emoji}")
        elif directions == "w":
            if player.current_room.e_to:
                player.current_room = player.current_room.e_to
                print(f"{walking}")
                print(
                    f"You have decided to go east and you moved to {player.current_room.name.upper()}")
                print(f"{player.current_room.describtion}")
            else:
                print(
                    f"⬅️  There is nothing west of {player.current_room.name.upper()}")
        elif directions == "q":
            print(f"{goodbye}")
            break
        else:
            print("Please select a valid direction")
    except ValueError:
        print("Please enter the valid direction")
