# Implement a class to hold room information. This should have name and
# description attributes.
class Room:

    def __init__(self, name, description):
        self.name: name
        self.description: description
    
    def __repr__(self):
        output = ""
        output += self.name     
        return output

myRoom = Room("Bedroom", "Where I get my beauty sleep.")
print(myRoom)