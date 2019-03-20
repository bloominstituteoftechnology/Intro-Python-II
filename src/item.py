'''
 class Item():
  def __init__(self, iId, name, iType, subType, baseMinDmg, baseMaxDmg, baseAcc, validJobs, validRaces, proc, stats, lore, tier):
    self.id = iId
    self.name = name
    self.type = iType
    self.subType = subType
    self.baseMinDmg = baseMinDmg
    self.baseMaxDmg = baseMaxDmg
    self.baseAcc = baseAcc
    self.validJobs = validJobs
    self.validRaces = validRaces
    self.proc = proc
    self.stats = stats
    self.lore = lore
    self.tier = tier
  def currentRoom(self):
    return '\n' + self.name + ', the ' + self.race + ' ' + self.job + ', stands near the... ' + self.Room.name + '\n\n~' + self.Room.description + '~\n'
'''
#rustySword = Item(1,"a rusty sword", "weapon", "sword", 1, 3, .5, 'f', 'e', None, None, None, 'c')


class Item():
  def __init__(self, id, name, description):
    self.id = id
    self.name = name
    self.description = description
  def __str__(self):
    return '#' + str(self.id) + ' ' + self.name + ', "' + self.description + '"'
