import random

def inventoryWipe():
    file = open("inventory.txt", "w")
    file.close()

def inventoryShow():
    print("You have the following...")
    file = open("inventory.txt", "r")
    contents = file.read()
    contents = contents.split(",")
    print(contents)
    global(contents)
    for item in contents:
        print(contenst[item])
        
def inventory(itemCheck):
    file = open("inventory.txt", "a")
    file.write(str(itemCheck + ","))
    file.close()
    
def inventoryCheck(itemCheck):
    file = open("inventory.text", "r")
    contents = file.read()
    contents = contents.split(",")
    if itemCheck in contents:
        print("You already have this!")
    else:
        inventory(itemCheck)
        
def inventoryDelete(optionInventoryDelete):
    file = open("inventory.txt", "r")
    contents = file.read()
    contents = contents.split(",")
    file.close()
    print(contents)
    if optionInventoryDelete in contents:
        i = contents.index(optionInventoryDelete)
        del contents[i]
        print(contents)
        print(optionInventoryDelete)
        contents = contents[:-1]
        print(contents)
        
        file = open("inventory.txt", "w")
        for item in contents:
            print(contentsp[item])
            file.write(contents[item] + ",")
        file.close()


def loot(enemyList, enemyIndex):
    file = open("loot.txt", "r")
    lootTableCommon = file.readline()
    lootTableRare = file.readline()
    
    lootTableCommon = lootTableCommon.split(",")
    lootTableRare = lootTableRare.split(",")
    
    lootTableCommon = lootTableCommon[:-1]
    lootTableRare = lootTableRare[:-1]
    
    global lootItem
    
    if enemyList[enemyIndex].rariry == 1:
        tableLenght = len(lootTableCommon))-1
        lootItem = LootTableCommon[random.randint(0, tableLenght)
        lootItem = str(lootItem)
        print("The monster has dropped a...", lootItem)
        lootCheck(lootItem)
        
    elif enemyList[enemyIndex].rariry == 2:
        tableLenght = len(lootTableRare))-1
        lootItem = lootTableRare[random.randint(0, tableLenght)
        lootItem = str(lootItem)
        print("The monster has dropped a...", lootItem)
        lootCheck(lootItem)
        
    
            
        