class Item:
    def __init__(item, name, description):
        item.name = name
        item.description = description

    def __str__(item):
        return f'{item.name}: {item.description}'
