# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        
    def __str__(self):
        return f"{self.name}\n {self.location}"
    
    def move(self, direction):
        if hasattr(self.location, f"{direction}_to"):
            #print(f"{direction}_to")
            self.location = getattr(self.location, f"{direction}_to")
            #print("location set to", self.location)
        if self.location is not None:
            self.location = self.location
        else:
            print("Please try a different direction.")