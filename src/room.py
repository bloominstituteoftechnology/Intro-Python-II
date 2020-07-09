# python room.py

class Room():
    def __init__(self, name, description, items = []):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None 

    def __repr__(self):
        return f"{self.name}.\nDescription: {self.description}"


# Items
items = {
"Outside Cave Entrance": ["backpack"], 
"Foyer": ["thread", "paintbrush","scarf"],
"Grand Overlook": ["flower"],
"Narrow Passage": ["flashlight"],
"Treasure Chamber": ["fork"],
"Kitchen": ["key", "apple"],
'Great Lake': ["fishing_rod"]
}




if __name__ == "__main__":
    room_1 = Room("Kitchen", "Place to cook meals")
    room_1.items=["knife", "stove"]
    room_2 = Room("Lake", "Place to fish", ["fishing_rod"])
    print(room_1)
    print(room_1.items)
    print(room_2)