# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, player_name, current_room, player_items=[]):
        self.player_name = player_name
        self.current_room = current_room
        self.player_items = player_items

    def movement(self, cardinal):
        next_room = getattr(self.current_room, f"{cardinal}_to")
        if next_room is not None:
            self.current_room = next_room

            print(self.current_room)
        elif next_room == None:
            print("Sorry, but you can not go that way")

    def take_secret_passage(self, basement):
        next_room = getattr(self.current_room, f"{basement}_to")
        if next_room is not None:
            self.current_room = next_room
            print(self.current_room)

    def take_items(self):
        if self.current_room.room_items is not None:
            for item in self.current_room.room_items:
                self.player_items.append(item)
            self.current_room.room_items.clear()
            # self.player_items.append(self.current_room.room_items)
            output = f'{self.player_name} has received: '
            for item in self.player_items:
                output += f'\n - {item}'
            print(output)

        # print(f"{self.player_name} has received {self.player_items}")

    def show_items(self):
        output = f"{self.player_name} has: "
        for item in self.player_items:
            str(item)
            output += f"\n - {item}"
        print(f'{output}')

    def drop_items(self):
        if self.player_items is not None:
            for item in self.player_items:
                self.current_room.room_items.append(item)
            self.player_items.clear()
            print(
                f'{self.player_name}! what are you doing?? you dropped all your items!')
        else:
            print('... you dont have any items to drop, go find something')

    def __str__(self):
        return f"hello, {self.player_name} you are currently in {self.current_room}"
