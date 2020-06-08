#> 
#> Main file
#>
from intro import *

class World():
    """Parent world class"""
    def __init__(self, name, description, items, north, south, east, west, light, encounter, trap, explored, intro):
        self._name = name
        self._description = description
        self._items = items
        self._north = north
        self._south = south
        self._east = east
        self._west = west
        self._light = light
        self._encounter = encounter
        self._trap = trap
        self._explored = explored
        self._intro = intro
        
    @property
    def name(self):
        return self._name
    @property
    def description(self):
        return self._description
    @property
    def items(self):
        return self._items
    @property
    def north(self):
        return self._north
    @property
    def south(self):
        return self._south
    @property
    def east(self):
        return self._east
    @property
    def west(self):
        return self._west
    @property
    def light(self):
        return self._light
    @property
    def encounter(self):
        return self._encounter
    @property
    def trap(self):
        return self._trap
    @property
    def explored(self):
        return self._explored
    @property
    def intro(self):
        return self._intro

    @name.setter
    def name(self, x):
        self._name = x
    @description.setter 
    def description(self, x):
        self._description = x
    @items.setter
    def items(self, x):
        self._items = x
    @north.setter
    def north(self, x):
        self._north = x
    @south.setter
    def south(self, x):
        self._south = x
    @east.setter
    def east(self, x):
        self._east = x
    @west.setter
    def west(self, x):
        self._west = x
    @light.setter
    def light(self, x):
        self._light = x
    @encounter.setter
    def encounter(self, x):
        self._encounter = x
    @trap.setter
    def trap(self, x):
        self._trap = x
    @explored.setter
    def explored(self, x):
        self._explored = x
    @intro.setter
    def intro(self, x):
        self._intro = x

    def __str__(self):
        return "{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}\n".format(
            self.name, self.description, self.items, self.north, self.south, self.east,
            self.west, self.light, self.encounter, self.trap, self.explored
        )

# class theOutskirts(World):
#     def __init__(self):
#         self._name = "Outskirts"
#         self._description = "A description of the Outskirts"
#         self._items = []
#         self._north = thePaleGate()
#         self._south = None
#         self._east = None
#         self._west = None
#         self._light = True
#         self._encounter = []
#         self._trap = False
#         self._explored = True
#         self._intro = ""
        
# class thePaleGate(World):
#     def __init__(self):
#         self._name = "Pale Gate"
#         self._description = "A description of the Pale Gate"
#         self._items = []
#         self._north = theAshbourneConcourse()
#         self._south = theOutskirts()
#         self._east = theBattlements()
#         self._west = None
#         self._light = True
#         self._encounter = []
#         self._trap = False
#         self._explored = False
#         self._intro = ""

# class theBattlements(World):
#     def __init__(self):
#         self._name = "Battlements"
#         self._description = "A description of the Battlements"
#         self._items = []
#         self._north = None
#         self._south = None
#         self._east = None
#         self._west = thePaleGate()
#         self._light = True
#         self._encounter = []
#         self._trap = False
#         self._explored = False
#         self._intro = ""

# class theAshbourneConcourse(World):
#     def __init__(self):
#         self._name = "Ashbourne Concourse"
#         self._description = "A description of the Ashbourne Concourse"
#         self._items = []
#         self._north = theTorchedHalls()
#         self._south = thePaleGate()
#         self._east = theBlacksmith()
#         self._west = theGrainCellars()
#         self._light = True
#         self._encounter = []
#         self._trap = False
#         self._explored = False
#         self._intro = ""

# class theBlacksmith(World):
#     def __init__(self):
#         self._name = "Blacksmith"
#         self._description = "A description of the Blacksmith"
#         self._items = []
#         self._north = None
#         self._south = None
#         self._east = None
#         self._west = theAshbourneConcourse()
#         self._light = True
#         self._encounter = []
#         self._trap = False
#         self._explored = False
#         self._intro = ""

# class theGrainCellars(World):
#     def __init__(self):
#         self._name = "Grain Cellars"
#         self._description = "A description of the Grain Cellars"
#         self._items = []
#         self._north = None
#         self._south = None
#         self._east = None
#         self._west = theAshbourneConcourse()
#         self._light = False
#         self._encounter = []
#         self._trap = False
#         self._explored = False
#         self._intro = ""

# class theTorchedHalls(World):
#     def __init__(self):
#         self._name = "Torched Halls"
#         self._description = "A description of the Torched Halls"
#         self._items = []
#         self._north = "hePaleThrone()
#         self._south = theAshbourneConcourse()
#         self._east = theReliquary()
#         self._west = theUndercroft()
#         self._light = True
#         self._encounter = []
#         self._trap = False
#         self._explored = False
#         self._intro = ""

# class theReliquary(World):
#     def __init__(self):
#         self._name = "Reliquary"
#         self._description = "A description of the Reliquary"
#         self._items = []
#         self._north = None
#         self._south = None
#         self._east = theProfaneShrine()
#         self._west = theAshbourneConcourse()
#         self._light = True
#         self._encounter = []
#         self._trap = False
#         self._explored = False
#         self._intro = ""

# class theProfaneShrine(World):
#     def __init__(self):
#         self._name = "Profane Shrine"
#         self._description = "A description of the Profane Shrine"
#         self._items = []
#         self._north = None
#         self._south = None
#         self._east = None
#         self._west = ""#theReliquary()
#         self._light = False
#         self._encounter = []
#         self._trap = False
#         self._explored = False
#         self._intro = ""

# class theUndercroft(World):
#     def __init__(self):
#         self._name = "Undercroft"
#         self._description = "A description of the Undercroft"
#         self._items = []
#         self._north = None
#         self._south = None
#         self._east = theTorchedHalls()
#         self._west = None
#         self._light = False
#         self._encounter = []
#         self._trap = False
#         self._explored = False
#         self._intro = ""

# class thePaleThrone(World):
#     def __init__(self):
#         self._name = "Pale Throne"
#         self._description = "A description of the Pale Throne"
#         self._items = []
#         self._north = theTerrace()
#         self._south = theTorchedHalls()
#         self._east = None
#         self._west = None
#         self._light = True
#         self._encounter = []
#         self._trap = False
#         self._explored = False
#         self._intro = ""

# class theTerrace(World):
#     def __init__(self):
#         self._name = "Terrace"
#         self._description = "A description of the Terrace"
#         self._items = []
#         self._north = theKerberosGate()
#         self._south = thePaleThrone()
#         self._east = None
#         self._west = None
#         self._light = True
#         self._encounter = []
#         self._trap = False
#         self._explored = False
#         self._intro = ""

# class theKerberosGate(World):
#     def __init__(self):
#         self._name = "Kerberos Gate"
#         self._description = "A description of the Kerberos Gate"
#         self._items = []
#         self._north = None
#         self._south = theTerrace()
#         self._east = None
#         self._west = None
#         self._light = True
#         self._encounter = []
#         self._trap = False
#         self._explored = False
#         self._intro = ""

# name, description, items, north, south, east, west, light, encounter, trap, explored, intro
dictWorld = { # North, South, East, West
    'theOutskirts' : World("the Outskirts", "A description of the Outskirts", [], 'thePaleGate', None, None, None, 
                    True, [],None, False, title_theOutskirts),
    'thePaleGate' : World("the Pale Gate", "A description of the Pale Gate", [], 'theAshbourneConcourse',
                    'theOutskirts', 'theBattlements', None, True, [], None, False, title_thePaleGate),
    'theBattlements' : World("the Battlements", "A description of the Battlements", [], None, None, None, 
                    'thePalgeGate', True, [], False, False, title_theBattlements),
    'theAshbourneConcourse' : World("the Ashbourne Concourse", "A description of the Ashbourne Concourse", [],
                    'theTorchedHalls', 'thePaleGate', 'theBlacksmith', 'theGrainCellars', True, [], False, False, title_theAshbourneConcourse),
    'theBlacksmith' : World("the Blacksmith", "A description of the Blacksm,ith", [], None, None, None, 
                    'theAshbourneConcourse', True, [], False, False, title_theBlacksmith),
    'theGrainCellars' : World("the Grain Cellars", "A description of the Grain Cellars", [], None, None, None, 
                    'theAshbourneConcourse', False, [], False, False, title_theGrainCellars),
    'theTorchedHalls' : World("the Torched Halls", "A description of the Torched Halls", [], 'thePaleThrone',
                    'theAshbourneConcourse', 'theReliquary', 'theUndercroft', True, [], False, False, title_theTorchedHalls),
    'theReliquary' : World("the Reliquary", "A description of the Reliquary", [], None, None, 'theProfaneShrine', 
                    'theAshbourneConcourse', False, [], False, False, title_theReliquary),
    'theProfaneShrine' : World("the Profane Shrine", "A description of the Profane Shrine", [], None, None, 
                    'theTorchedHalls', None, False, [], False, False, title_theProfaneShrine),
    'thePaleThrone' : World("the Pale Throne", "A description of the Pale Thrones", [], 'theTerrace', 
                    'theTorchedHalls', None, None, True, [], False, False, title_thePaleThrone),
    'theTerrace' : World("the Terrace", "A description of the Terrace", [], 'theKerberosGate','thePaleThrone', 
                    None, None, True, [], False, False, title_theTerrace),
    'theKerberosGate' : World("the Kerberos Gate", "A description of the Kerberos Gate", [], None, 'theTerrace', None, 
                    None, True, [], False, False, title_theKerberosGate)
}

if __name__ == "__main__":
    pass