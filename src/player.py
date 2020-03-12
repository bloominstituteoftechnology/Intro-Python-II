"""
BeWilder - text adventure game :: Player definition

Write a class to hold player information.
e.g. what room they are in currently.
"""

import sys

from room import Room


class Player:
    def __init__(self, name: str, current_room: Room):
        """Constructor for the Player base class.
        
        :param current_room (str) : The player's current room, defaults to 'outside'.
        """
        self.name = name
        # Set the initial room by "moving" into it, thus printing the room info
        self.move(current_room)

    def move(self, dst_room: Room):
        """Moves the player to a new room.
        
        :param dst_room (Room) : The player's destination room.
        """
        self.current_room = dst_room
        print(f"\n{self.current_room}")

    def take_action(self, cmd: str):
        """Take action by key command.
        
        :param cmd (str) : Key command from user.
        :param player (Player) : Instance of Player which will take the action.
        :return (None) : Calls the appropriate function.
        """
        room_lookup = {
            "n": self.current_room.n_to,
            "s": self.current_room.s_to,
            "e": self.current_room.e_to,
            "w": self.current_room.w_to,
        }

        if cmd == "q":
            print("Exiting game...")
            sys.exit(0)

        # Look up destination room and move the player into it
        dst = room_lookup[cmd]
        if dst:
            self.move(dst)
        else:
            print("No room exists in that direction!")

