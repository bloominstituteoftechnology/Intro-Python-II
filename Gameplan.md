1. Adventure
    a. user input executes actions (like rps)
    b. implement 2 word commands(parser)
    c. Add get and drop commands to parser
        (Example: drop hammer, get hammer)
        (get Item)
    d. get/take input maps the list to see if item is           available in that room
2. Player
    a. Hold an inventory list
    b. get/take command 
    c. drop command
    d. i/inventory command shows list of items carried by player
3. Room
    a. Loop? when player enters, print out all items that are "visible" to player"
    b. "item" list
    c. add item to room
    d. when player takes item, room - item

4. Items
    a. name
    b. attribute
    c. placement? Player or Room
        on_take: when picked up by player
        on_drop: when player drops item
    d. If item is unavailable message: item is not available