# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, roomID, name, description, items):
        self.roomID = roomID
        self.name = name
        self.description = description
        self.items = []

    def __repr__(self):
        return f"""roomID: {self.roomID}, name: {self.name}, 
        description: {self.description}"""

    def look(self):
        updateItems = []

        for item in self.items:
            itemName = item

            print(f"Look what you found: {itemName}")
            playerChoice = input("Would you like to pick up the item?: y/n")
