# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room:
    def __init__ (self, name, description):
        self.name = name
        self.description = description
        self.inventory = []
    def __repr__ (self):
        return f"Name: {self.name}, description: {self.description}"

#instances of Room 
o = Room("Outside", "North of you, the cave mount beckons")
f = Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""")
t =  Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")
ov = Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""")
n = Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""")


#tying location attribute to room instances, and item instances to each room
#basically same as defining below init, as self.---

#outside
o.n_to = f
o.inventory = [Item("key", """key to treasure box"""),Item("lantern", """a light to guide you"""),]

#foyer
f.s_to = o
f.n_to = ov
f.e_to = n
f.inventory = [Item("wand", """just in case you need magic"""),Item("shield", """to protect you"""),]

#overlook
ov.s_to = f
ov.inventory = [Item("cape", """because it's cold out here"""),Item("snack", """because low blood sugar"""),]

#narrow passage
n.w_to = f
n.n_to = t
n.inventory =[Item("beer", """who doesn't want beer in narrow passages??"""),Item("diamond", """because shiny"""),]

#treasury 
t.s_to = n
t.inventory =[Item("gold", """it's about time this pays off"""),Item("job offer", """ongoing income is always nice"""),]

