from item import Item


class Fixed(Item):
    def __init__(self, name, description, danger_message="", removed_message=""):
        super().__init__(name, description)
        self.blocking_path = None   # if this item is blocking a path, string n|e|s|w

        # set to True if it can hurt the player when they interact
        if danger_message == "":
            self.dangerous = False
        else:
            self.dangerous = True
        self.danger_message = danger_message  # message to display if player is hurt

        if removed_message == "":
            self.remove_when_used = False
        else:
            # should be removed when associated Prop is used
            self.remove_when_used = True
        self.removed = False
        self.removed_message = removed_message  # displays when item is removed

        self.open_when_used = False     # should be opened when associated Prop is used
        self.opened = False
        self.item_inside = None     # when opened, this Item replaces it

        self.used_with = None    # what Prop does this Fixed item interact with?

    def use(self, with_prop):
        if self.used_with == with_prop:
            if self.remove_when_used:
                self.blocking_path = None
                self.removed = True
            if self.open_when_used:
                self.opened = True
                self.item_inside.hidden = False
                # print(f'The {self.name} opened. {prop.a_or_an} {prop.name} was revealed! 🎉')
                self.item_inside = None     # the item is just in the room now
            return True
        elif self.dangerous:
            print(self.danger_message)
            return False
        else:
            return False

    def __str__(self):
        val = ''
        if not self.removed:
            val = f'There is {self.a_or_an()} {self.name} here. {self.description}.'
            if self.dangerous:
                val += ' It looks dangerous.'
            if self.blocking_path != None:
                val += ' It is blocking the way '
                if self.blocking_path == 'n':
                    val += 'North.'
                if self.blocking_path == 'e':
                    val += 'East.'
                if self.blocking_path == 's':
                    val += 'South.'
                if self.blocking_path == 'w':
                    val += 'West.'
            if self.opened:
                val += ' It is opened.'
        return val
