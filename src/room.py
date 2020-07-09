# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, roomID, name, description, items):
        self.roomID = roomID
        self.name = name
        self.description = description
        self.items = []

    def look(self):
        updateItems = []

        for item in self.items:
            itemName = item[0]

            print(f"Look what you found: {itemName}")
            playerChoice = input("Would you like to pick up the item?: y/n")

            if (playerChoice == 'y'):
                print(f"You have added {itemName} to your inventory!")
                self.items.pop(itemName)
                updateItems = itemName

            elif (action == 'n'):
                print(f"You chose not to take any items from this room!")

            else:
                print("Bad User Input - Please enter a valid input!")

        return updateItems

    def __repr__(self):
        return f"""roomID: {self.roomID}, name: {self.name}, 
        description: {self.description}"""
