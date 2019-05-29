# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
   name = ""
   current_room: "outside"

   def change_name(self, name):
      self.name = name
   def move_room(self, new_room):
      self.current_room = new_room