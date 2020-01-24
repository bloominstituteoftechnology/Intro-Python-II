# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(room, name, description, n_to = 0, s_to = 0, e_to = 0, w_to = 0):
        room.name = name
        room.description = description
        room.n_to = n_to
        room.s_to = s_to
        room.w_to = w_to
        room.e_to = e_to

    def __str__(room):
        str = f'{room.name}: {room.description}'
        return str

    def add_item(room, item):
        room.item.append(item)

    def print_item(room):
        print("Items in this room: ")
        if len(room.item) > 0:
            for i in room.item:
                print (i.name, i.description)
        else:
            print("There are no items in this room!")

    def remove_item(room, item):
        room.item.remove(item)
