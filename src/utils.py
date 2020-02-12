from rooms import rooms


def find_key(value):
    for k, v in rooms.items():
        if v == value:
            return k