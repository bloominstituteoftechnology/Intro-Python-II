# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, n_to, s_to, e_to, w_to):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
    def __repr__(self):
        # name
        # 1. + categories[0]
        # 2. + categories[1]
        output = ""
        output += self.name + "\n"
        i = 1
        for d in self.description:
            output += str(i) +". " + d + "\n"
            i += 1
        output += str(i) + ". Exit"
        return output

#Example
my_room = Room("Example Room", ["doors", "knobs", "walls", "table" ])
print(my_room)

selection = 0
while int(selection) != len(my_room.descriptions) +1:
    selection = input("Select a room: ")
    #TRY/EXCEPT ERROR HANDLING
    try:
        selection = int(selection)
        if selection == len(my_room.descriptions)+1:
            print("Thanks for visiting!")
        elif selection >= 1 and selection <= len(my_room.descriptions) +1:  #INPUTS ARE ALWAYS STRINGS
            #print("The player selected " + str(selection))
            print(my_room.descriptions[selection-1])
        else:
            print("Please select a valid room")
    except ValueError:
        print("Please enter your choice as a number.")
        #allows user to reenter a new value