class Room:

    def __init__(self, location, dialog, strName=True, n_to=None, e_to=None, s_to=None, w_to=None):
        self.location = location
        self.dialog = dialog
        self.strName = strName

# True strName returns Room.name, False returns dialog
    def __str__(self):
        if self.strName:
            return """{self.location}\n""".format(self = self)
        else:
            return """{self.dialog}\n""".format(self = self)
    
    def changeStr(self):
        if self.strName:
            self.strName = False
        else:
            self.strName = True