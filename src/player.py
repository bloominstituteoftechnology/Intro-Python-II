# Write a class to hold player information, e.g. what room they are in
# currently.

#Game plan 
# create a class by the name of player 
# what important info should your player have 
# name, skill, current room 
#                                             

class Player:
     def __init__(self, name, current_room): # initiate values to object properties 
      self.name = name
      #self.skill = skill
      self.current_room = current_room 


     def myplayer(self):
         print("Hello my name is " + self.name + " and I am located " + self.current_room) #function that belongs to the Player object that we created  
p1 = Player("Zuri", "outside")
p1.myplayer()