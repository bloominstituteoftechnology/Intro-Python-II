# Add a subclass to Item called LightSource.
# During world creation, add a lamp LightSource to a convenient Room.
# Override on_drop in LightSource that tells the player "It's not wise to drop your source of light!" if the player drops it. (But still lets them drop it.)
# Add an attribute to Room called is_light that is True if the Room is naturally illuminated, or False if a LightSource is required to see what is in the room.
# Modify the main loop to test if there is light in the Room (i.e. if is_light is True or there is a LightSource item in the Room's contents or if there is a LightSource item in the Player's contents).
# If there is light in the room, display name, description, and contents as normal.
# If there isn't, print out "It's pitch black!" instead.
# Hint: isinstance might help you figure out if there's a LightSource among all the nearby Items.
# Modify the get/take code to print "Good luck finding that in the dark!" if the user tries to pick up an Item in the dark.


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_drop(self, item):
        print(f"{item.name} has been dropped 💣")


class LightSource(Item):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.name = name

    def on_drop(self):
        print("It's not wise to drop your source of light!")
