# Write a class to hold player information, e.g. what room they are in
# currently.
import sys, time

class Player:
  def __init__(self, name, current_room):
    self.name = name
    self.current_room = current_room
  
  def wait(self, count):
    for _ in range(count):
      sys.stdout.write(".")
      sys.stdout.flush()
      time.sleep(0.1)

  def travel(self, direction):
    if direction != None:
      self.wait(5)
      print(f"\nYou're headed for {direction.name}", sep="")
      self.wait(11)
      self.current_room = direction
    else:
      self.wait(5)
      print("\nYou can't go there!")
      self.wait(5)