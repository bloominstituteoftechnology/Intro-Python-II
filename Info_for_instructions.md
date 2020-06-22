# Internal Project Instructions Per File 

## `` adv.py ``
 Make a new player object that is currently in the 'outside' room.
 </br>

 Write a loop that:

* Prints the current room name
* Prints the current description (the textwrap module might be useful here).
* Waits for user input and decides what to do.

If the user enters a cardinal direction, attempt to move to the room there.
Print an error message if the movement isn't allowed.

If the user enters "q", quit the game.

```
#-------------------------------|
#  Format for printing dialog   |
#       of current room         |
#   print(room['treasure'])     |
#-------------------------------|

#------------------------------------------------------------|
#  Format for changing current room                          |
#   playerVar.current_room = room['newSelection'].location   |
#------------------------------------------------------------|
```
# `` room.py ``

Implement a class to hold room information. This should have name and
description attributes.


# `` player.py ``
Write a class to hold player information, e.g. what room they are in currently.

player needs:
* Name
* Current Room 