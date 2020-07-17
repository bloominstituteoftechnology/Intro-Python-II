# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, in_room):
        self.name = name
        self.in_room = in_room
        self.props = {}
        self.alive = True

    def pick_up(self, prop):
        if len(self.props) > 2:
            print('❌ You cannot carry more than three items. Maybe drop something?')
            prop.held = False
            return False
        else:
            self.props[prop.name.lower()] = prop
            print(f'\n\n🙌 You picked up the {prop.name}.')
            prop.held = True
            return True

    def put_down(self, prop_name):
        if prop_name in self.props:
            prop = self.props[prop_name]
            del self.props[prop.name.lower()]
            print(f'\n\n👇 You put down the {prop_name}')
            prop.held = False
            return prop
        else:
            print(f"\n\n🤦 You weren't holding the {prop.name}!")
            return None

    def die(self):
        self.alive = False
        print('💀You died.')

    def use_prop(self, prop, fixed):
        success = fixed.use(prop)     # use the prop on the fixed item
        if not success and fixed.dangerous:
            self.die()
        elif not success and not fixed.dangerous:
            print('🤷 Nothing happened.')

    def use_fixed(self, fixed):
        if fixed.dangerous:
            self.die()
