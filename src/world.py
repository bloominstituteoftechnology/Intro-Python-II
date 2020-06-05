class World():
    """Parent world class"""
    def __init__(
        self, name, description, items, south, north, east, west, light, encounter,
        trap, explored
    ):

        self.name = name
        self.description = description
        self.items = items
        self.south = south
        self.north = north
        self.east = east
        self.west = west
        self.light = light
        self.encounter = encounter
        self.trap = trap
        self.explored = explored

        def getName(self):
            return self.name
        def getDescription(self):
            return self.description
        def getItems(self):
            return self.items
        def getSouth(self):
            return self.south
        def getNorth(self):
            return self.north
        def getEast(self):
            return self.east
        def getWest(self):
            return self.west
        def getLight(self):
            return self.light
        def getisEncounter(self):
            return self.encounter
        def getTrap(self):
            return self.trap
        def getisExplored(self):
            return self.explored

        def setName(self, newName):
            self.name = newName 
        def setDescription(self, newDescription):
            self.description = newDescription
        def setItems(self, newItems):
            self.items = newItems
        def setSouth(self, newSouth):
            self.south = newSouth
        def setNorth(self, newNorth):
            self.north = newNorth
        def setEast(self, newEast):
            self.east = newEast
        def setWest(self, newWest):
            self.west = newWest
        def setLight(self, newLight):
            self.light = newLight
        def setEncounter(self, newEncounter):
            self.encounter = newEncounter
        def setTrap(self, newTrap):
            self.trap = newTrap
        def setExplored(self, newExplored):
            self.explored = newExplored

    def __str__(self):
        return "{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}\n".format(self.name, 
                                                                    self.description,
                                                                    self.items,
                                                                    self.south,
                                                                    self.north,
                                                                    self.east,
                                                                    self.west,
                                                                    self.light,
                                                                    self.encounter,
                                                                    self.trap,
                                                                    self.explored
                                                                    )


class theOutskirts(World):
    def __init__(self):
        super().__init__(name="Outskirts",
                        description="A description of the Outskirts",
                        items=[],
                        south=None,
                        north="Blasted Gate",
                        east=None,
                        west=None,
                        light=True,
                        encounter=[],
                        trap=False,
                        explored=True
                        )


class theBlastedGate(World):
    def __init__(self):
        super().__init__(name="Blasted Gate",
                        description="A description of the Blasted Gates",
                        items=[],
                        south=None,
                        north="Solitary Fountain",
                        east="Blasksmith",
                        west="Sepulcher",
                        light=True,
                        encounter=[],
                        trap=False,
                        explored=False
                        )


class theSolitaryFountain(World):
    def __init__(self):
        super().__init__(name="Solitary Fountain",
                        description="A description of the Solitary Fountain",
                        items=[],
                        south="Blasted Gate",
                        north="Estate",
                        east="Blacksmith",
                        west="Sepulcher",
                        light=True,
                        encounter=[],
                        trap=False,
                        explored=False
                        )


class theSepulcher(World):
    def __init__(self):
        super().__init__(name="The Sepulcher",
                        description="A description of the Sepulcher",
                        items=[],
                        south=None,
                        north=None,
                        east="Solitary Fountain",
                        west=None,
                        light=False,
                        encounter=[],
                        trap=False,
                        explored=False
                        )


class theBlacksmith(World):
    def __init__(self):
        super().__init__(name="Blacksmith",
                        description="A description of the Blacksmith",
                        items=[],
                        south=None,
                        north=None,
                        east=None,
                        west="Solitary Fountain",
                        light=True,
                        encounter=[],
                        trap=False,
                        explored=False
                        )


class theEstate(World):
    def __init__(self):
        super().__init__(name="Estate",
                        description="A description of the Estate",
                        items=[],
                        south="Solitary Fountain",
                        north="Torched Halls",
                        east=None,
                        west=None,
                        light=True,
                        encounter=[],
                        trap=False,
                        explored=False
                        )


class theTorchedHalls(World):
    def __init__(self):
        super().__init__(name="Torched Halls",
                        description="A description of the Torched Halls",
                        items=[],
                        south="Estate",
                        north="Pale Throne",
                        east="Reliquary",
                        west="Cellar",
                        light=True,
                        encounter=[],
                        trap=False,
                        explored=False
                        )


class theCellar(World):
    def __init__(self):
        super().__init__(name="Cellar",
                        description="A description of the Cellar",
                        items=[],
                        south=None,
                        north=None,
                        east="Torched Halls",
                        west=None,
                        light=False,
                        encounter=[],
                        trap=False,
                        explored=False
                        )


class theReliquary(World):
    def __init__(self):
        super().__init__(name="Reliquary",
                        description="A description of the Reliquary",
                        items=[],
                        south=None,
                        north=None,
                        east="Overlook",
                        west="Torched Halls",
                        light=True,
                        encounter=[],
                        trap=False,
                        explored=False
                        )


class theOverlook(World):
    def __init__(self):
        super().__init__(name="Overlook",
                        description="A description of the Balcony",
                        items=[],
                        south=None,
                        north=None,
                        east="Narrow Passage",
                        west="Reliquary",
                        light=True,
                        encounter=[],
                        trap=False,
                        explored=False
                        )


class theNarrowPassage(World):
    def __init__(self):
        super().__init__(name="Narrow Passage",
                        description="A description of the Narrow Passage",
                        items=[],
                        south=None,
                        north=None,
                        east="Shrine",
                        west="Overlook",
                        light=True,
                        encounter=[],
                        trap=False,
                        explored=False
                        )


class theShrine(World):
    def __init__(self):
        super().__init__(name="Shrine",
                        description="A description of the Shrine",
                        items=[],
                        south=None,
                        north=None,
                        east=None,
                        west="Narrow Passage",
                        light=True,
                        encounter=[],
                        trap=False,
                        explored=False
                        )


class thePaleThrone(World):
    def __init__(self):
        super().__init__(name="Pale Throne",
                        description="A description of the Pale Throne",
                        items=[],
                        south="Torched Halls",
                        north="Balcony",
                        east=None,
                        west=None,
                        light=True,
                        encounter=[],
                        trap=False,
                        explored=False
                        )


class theBalcony(World):
    def __init__(self):
        super().__init__(name="Balcony",
                        description="A description of the Balcony",
                        items=[],
                        south="Pale Throne",
                        north="Pale Gate",
                        east=None,
                        west=None,
                        light=True,
                        encounter=[],
                        trap=False,
                        explored=False
                        )


class thePaleGate(World):
    def __init__(self):
        super().__init__(name="Pale Gate",
                        description="A description of the Pale Gate",
                        items=[],
                        south="Balcony",
                        north=None,
                        east=None,
                        west=None,
                        light=True,
                        encounter=[],
                        trap=True,
                        explored=False
                        )


if __name__ == "__main__":
    ##### Class Declaration ######
    theOutskirts = theOutskirts()
    theBlastedGate = theBlastedGate()
    theSolitaryFountain = theSolitaryFountain()
    theSepulcher = theSepulcher()
    theBlacksmith = theBlacksmith()
    theEstate = theEstate()
    theTorchedHalls = theTorchedHalls()
    theCellar = theCellar()
    theReliquary = theReliquary()
    theOverlook = theOverlook()
    theNarrowPassage = theNarrowPassage()
    theShrine = theShrine()
    thePaleThrone = thePaleThrone()
    theBalcony = theBalcony()
    thePaleGate = thePaleGate()