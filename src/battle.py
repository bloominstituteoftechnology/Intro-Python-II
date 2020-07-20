import random
import time

from utils import clear, space_word
from monster import Monster
from player import Player

class Battle:

    def __init__(self, player, monsters):
        self.player = player
        self.monsters = monsters

    def display_stats(self):
        spaces = 12
        monsters_names = ""
        monsters_hp = ""
        player_name = space_word("player", spaces)
        for monster in self.monsters:
            monsters_names += space_word(monster.name, spaces)
            monsters_hp += space_word(monster.base_hp, spaces)
        return f"{monsters_names}\n{monsters_hp}\n-------------------\n\
{player_name}\n{self.player.base_hp}"

    def calculate_damage(self, user, skill, target):
        total_damage = user.base_attack + user.boosted_attack + skill.damage
        damage_taken =  total_damage - target.base_defense - target.boosted_defense
        if damage_taken > 0:
            target.base_hp -= damage_taken
            return damage_taken
        return "0"


    def player_move(self):
        player_input = input(f"Select your move:\n{self.player.list_skills()}\n")
        while player_input in self.player.skills:
            targets = [f"{self.monsters[i].name} {i + 1}" for i in range(len(self.monsters))]
            target = int(input(f"Select target (input number): {targets}")) - 1
            if targets[target]:
                selected_target = self.monsters[target]
                skill = self.player.skills[player_input]
                clear()
                print(f"player {skill.on_skill_call()} on {selected_target.name}")
                attack_res = self.calculate_damage(self.player, skill, selected_target)
                print(f"{selected_target.name} took {attack_res} damage")
                return
        self.player_move()

    def monster_move(self, monster):
        time.sleep(1)
        skill = monster.skills[random.choice(list(monster.skills))]
        print(f"{monster.name} {skill.on_skill_call()} on player")
        attack_res = self.calculate_damage(monster, skill, self.player)
        print(f"Player took {attack_res} damage")
        time.sleep(1)