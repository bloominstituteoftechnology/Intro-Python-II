class Room:
    def __init__(self, name, description, n_to, s_to, e_to, w_to):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.w_to = w_to
        self.e_to = e_to

    def __repr__(self):
        return self.name + " - " + self.description


East_Port = Room("East Portico", "Welcome to The Manor.", None, "Enterance Hall", None, None)
Enterance_Hall = Room("Enterance Hall", "Please come in.", "East Portico", "Parlor", "Drawing Room", "Library")
Parlor = Room("Parlor", "Gossip and tea served daily.", "Enterance Hall", "West Poritco", "Master Bedroom", "Dining Hall")
West_Port = Room("West Portico", "Take in a view of the gardens.", "Parlor", None, None, None)
Library = Room("Library", "All manners of Manor's business are conducted in the library.", None, "", "Enterance Hall", None)
Dining_Hall = Room("Dining Hall", "Join us for a feast or just a bite to eat.", "Library", None, "Parlor", "Guest Room")
Guest_Room = Room("Guest Room", "Stay awhile.", None, None, "Dining Hall", "North Terrace")
North_Terrace = Room("North Terrace", "Lovely views of the nearby village.", None, None, "Guest Room", None)
Drawing_Room = Room("Drawing Room", "Looking for a quiet spot to read or embroider? You've found the spot.", None, "Master Bedroom", None, "Enterance Hall")
Master_Bedroom = Room("Master Bedroom", "Where the Lord and Lady of The Manor take their rest.", "Drawing Room", None, "Greenhouse", "Parlor")
Greenhouse = Room("Greenhouse", "The finest tomatoes in the parish.", None, None, "Master Bedroom", "South Terrace")
South_Terrace = Room("South Portico", "Vistas overlooking the pond.", None, None, None, "Greenhouse")