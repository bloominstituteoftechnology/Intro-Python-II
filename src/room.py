# Implement a class to hold room information. This should have name and
# description attributes.
from collections import  deque


class Room(object):
    """A room in the game.

    :var name: str - name of the room
    :var description: str - description of room

    """

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description
        self.items_ = {}
        self.characters = {}
        self.light = True
        self.to_n = None
        self.to_s = None
        self.to_w = None
        self.to_e = None


class Arena(Room):
    """A room to battle in.

    Inherits from Room

    """

    def battle(self):
        """A fight to the death!"""
        battle_q = deque()
        for player in self.characters:
            battle_q.append(self.characters[player])
        while not any(player.hp <= 0 for player in battle_q):
            attacker = battle_q.popleft()
            attackee = battle_q.popleft()

            attacker.attack(attackee)

            battle_q.append(attackee)
            battle_q.append(attacker)
