#room instance needs to accept string parameters name and desc

class Room: 
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return f"{self.name}, {self.description}"