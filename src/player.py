# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room
from random import choice

class Player():
    """Player for CLI text adventure game
    
    Methods:
        __init__: Initialize Player Class
        move: Move to new location, a different Room"""

    def __init__(self, playerName, location, items=[]):
        """Initialize Player class
        
        Args:
            location: instantiated Room class in adventure game
            
        Returns:
            Instantiated Player class
            
        Usage:
            example = Room(name="Kitchen", 
                           description="Splendid aromas emanate from within")

            another_example = Room("Living Room", 
                                   "Much Netflixing occurs within these walls")

            example.n_to = another_example
            another_example.s_to = example

            player = Player(example)
    """

        self.playerName = playerName
        self.location = location
        self.health = 100
        self.experience = 0
        self.items = items
    
    @property
    def browse_room_contents(self):
        return self.location.loot

    def loot(self):
        self.items.append(self.location.loot)
        print("Your treasure grows! Here is your updated inventory:\n\n")
        self.location.empty_room_contents()
        return self.items

    def move(self, cardinal_direction):
        """Move to new location, a different Room in the adventure game
        
        Args:
            cardinal_direction: n (North), s (South), e (East), or w (West) to move between rooms
            
        Returns: 
            Updated location in adventure game

        Usage:
            player.move("n")

        """

        monster_nouns = ["Orc","Goblin","Demon","Imp","Creature","Fiend","Monster","Gremlin"]
        monster_adjectives = ["Gaging","Furious","Angry","Ravenous","Infuriated","Blood-Thirsty"]
        monster_verbs = ["patrolled","guarded","blocked"]

        new_location = self.location.get_neighbor(cardinal_direction)

        if new_location != None:
            self.location = new_location
        
        else:
            print("\nYour path is {} by {} {}, please choose another direction to stay alive".format(choice(monster_verbs), 
                                                                                                   choice(monster_adjectives), 
                                                                                                   choice(monster_nouns)))

