import Foundation

class Item {
    let name: String
    let description: String
    
    init(_ itemName: String, itemDescription: String) {
        name = itemName
        description = itemDescription
    }
    
    func taken() {
        print("Picked up \(name). May it serve you well.")
    }
    
    func dropped() {
        print("Dropped \(name). Hope you didn't need that.")
    }
    
    func examine() {
        print("""
            Examining the \(name)...
            \(description)
            """)
    }
}

class Room {
    var nTo: Room? = nil
    var sTo: Room? = nil
    var eTo: Room? = nil
    var wTo: Room? = nil
    
    name: String
    description: String
    var items: [Item]
    
    init(_ roomName: String, roomDescription: String) {
        items = [Item]()
        name = roomName
        description = roomDescription
    }
    
    func addItem(_ item: Item) {
        items.append(item)
    }
    
}

class Player {
    let name: String
    var currentRoom: Room
    var inventory: [Item]
    
    init(_ newName: String, in room: Room) {
        name = newName
        currentRoom = room
        inventory = [Item]()
    }
    
    func status() {
        print("\(name) is currently in \(room)")
    }
    
    func changeRoom(_ direction: String) {
        switch direction{
        case "n":
            guard currentRoom.nTo != nil else {print("Your adventure lies elsewhere \(name)."); return }
            currentRoom = currentRoom.n_to
        case "s":
            guard currentRoom.sTo != nil else {print("Your adventure lies elsewhere \(name)."); return }
            currentRoom = currentRoom.s_to
        case "e":
            guard currentRoom.eTo != nil else {print("Your adventure lies elsewhere \(name)."); return }
            currentRoom = currentRoom.e_to
        case "w":
            guard currentRoom.wTo != nil else {print("Your adventure lies elsewhere \(name)."); return }
            currentRoom = currentRoom.w_to
        default:
            NSLog("Invalid direction")
            break
        }
    }
    
    func look() {
        var roomItems: String {
            var itemsString =""""""
            
            for item in currentRoom.items {
                itemsString.append(
                    """
                    
                    \(item.name)
                    """)
            }
            return itemsString
        }
        print(
            """
            \(name), you find yourself in \(currentRoom.name)
            In this room you see the following:
            \(roomItems)
            """)
    }
    
    func showInventory() {
        switch inventory.count {
        case 0:
            print("You haven't picked up anything yet, \(name)")
        case 1:
            print("You have 1 item in your inventory, \(name)")
        default:
            print("You have \(String(inventory.count)) items in your inventory.")
        }
    }
    
    func selectRoomItem(_ item: String) -> Item? {
        for i in currentRoom.items {
            if i.name.lower() == item.lower() {
                return i
            } else {
                print("\(item) not found.")
                return nil
            }
        }
    }
    
    func selectInventoryItem(_ item: String) -> Item? {
        for i in inventory {
            if i.name.lower() == item.lower() {
                return i
            } else {
                print("\(item) not found.")
                return nil
            }
        }
    }
    
    func take(_ item: Item) {
        inventory.append(item)
        currentRoom.items.remove(item)
        item.taken()
    }
    
    func drop(_ item: Item) {
        currentRoom.items.append(item)
        inventory.items.remove(item)
        item.dropped()
    }
}

var player: Player?
let directions = ["n", "s", "e", "w"]
let ations = ["take", "drop"]
var loop: Bool? = nil

var room: [String : Room] = ["outside" : Room("Outside Cave Entrance",
                                              description: "North of you, the cave mount beckons"),
                             "foyer" : Room("Foyer",
                                            description: "Dim light filters in from the south. Dusty passages run north and east."),
                             "overlook" : Room("Grand Overlook",
                                               description: "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."),
                             "narrow" : Room("Narrow Passage",
                                             description: "The narrow passage bends here from west to north. The smell of gold permeates the air."),
                             "treasure" : Room("Treasure Chamber",
                                               description: "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.")]

func setUpRooms() {
    room["outside"].nTo = room["foyer"]
    room["foyer"].sTo = room["outside"]
    room["foyer"].nTo = room["overlook"]
    room["foyer"].eTo = room["narrow"]
    room["overlook"].sTo = room["foyer"]
    room["narrow"].wTo = room["foyer"]
    room["narrow"].nTo = room["treasure"]
    room["treasure"].sTo = room["narrow"]
}

func addItemsToRooms() {
    room["outside"].addItem(Item("Torch", "A light to guide you through the darkness, \(player.name)"))
    room["foyer"].addItem(Item("Shield", "A large oak shield painted red with a white chevron crossing it."))
    room["overlook"].addItem(Item("Map", "Perhaps this will help us find our way."))
    room["narrow"].addItem(Item("Sword", "Arm yourself with knowledge, \(player.name), it may serve you better than steel!"))
    room["treasure"].addItem(Item("Book", """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better tha
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""))
}

func setPlayer() {
    let playerName = String(readLine("What is your name adventurer? "))
    player = Player(playerName,
                    in: room["outside"])
    
    print("To move around the map, press 'n', 'e', 's', 'w'. Look for items to help on your way. For help try 'Help' or 'h'.")
    print("Good luck, \(player.name)")
}

setUpRooms()
addItemsToRooms()
setPlayer()
player.look()
loop == true

while loop == true {
    var userInput = readLine("Where would you like to go, \(player.name)?").lower().split()
    
    if userInput.count > 2 || userInput.count < 1 {
        print("Sorry, \(player.name), that's not a valid one or two word command. Would you like 'help'?")
    } else if userInput.count == 2 {
        if userInput[0] in actions {
            if userInput[0] == "t" || userInput == "take" {
                let item = player.selectRoomItem(userInput[1])
                player.take(item)
            } else if userInput[0] == "d" || userInput[0] == "drop" {
                item = player.selectInventoryItem(userInput[1])
                player.drop(item)
            }
        }
    } else {
        if userInput[0] == "q" || userInput == "quit" {
            print(f"Thanks for playing {player.name}!")
            loop == false
            break
        } else if userInput[0] == "h" || userInput[0] == "help" {
            print("""
Commands:
'n' - Move North
's' - Move South
'e' - Move East
'w' - Move West
't' or 'take' '<item>' - Take Item
'd' or 'drop' '<item>' - Drop Item
'inv' or 'inventory' - Examine Inventory Items
'l' or 'look' - Look around the current room
'h' or 'help' - Help Menu
'q' or 'quit' - Exit Game
""")
            continue
        } else if userInput[0] == "l" || userInput[0] == "look" {
            player.look()
            continue
        } else if userInput[0] == "inv" || userInput[0] == "inventory" {
            player.showInventory()
            continue
        } else if userInput in directions {
            player.changeRoom(userInput[0])
            player.look()
        } else {
            print("Movement not allowed. Please enter a direction (n, s, e, w) to move around the map.")
        }
    }
}
