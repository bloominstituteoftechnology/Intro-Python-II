from room import Room, Arena
from item import Item, Container, SlingShot, Pebbles, Berries

# Declare rooms in rooms dict.
rooms = {
    'rest_stop': Room("\nYou are at a North Cascades Hwy rest-stop. It is a crisp fall morning.",
                      "North of you, a little dog barks and dashes down a forest trail. \nTo the South, your warm car "
                      "and the open road."),

    'car': Room("You head down the road, wondering what could have been.",
                "An 18 wheeler crushes you. Look both ways before entering traffic."),

    'forest_trail': Room("The trail opens to snow capped peaks and a lush valley.",
                         "To the North, a wild river runs \nOther trails lead to the East and West. \nReturn to the "
                         "parking lot to the South."),

    'river_bank': Room("The clear, cold Skagit river rushes at your feet.",
                       "Attempt to ford the river by heading North \nHead upstream to the East \nMove toward the "
                       "Puget Sound by heading downstream, to the West. \nGo back toward the start by moving South"),

    'trail_east': Arena("A massive peak looms above.",
                        "Climb the peak by continuing East. \nHead North along Kendal Catwalk. \nTo the South is the "
                        "difficult Section K of the Pacific Crest Trail. \nThe sweeping valley vistas lie to the West"),

    'trail_west': Room("The trail forks at a granite outcropping.",
                       "A short climb West looks like the entrance to a cave. \nThe trail continues both North and "
                       "South. \nHead back to the valley views to the East"),

    'kendal_catwalk': Room("A narrow walkway juts out from the shear cliff, to fall hear is certain death.",
                           "An avalanche has blocked your path. \nYou must return to the South"),

    'section_k': Room("This difficult trail seems to go on forever.",
                      "Continue into the unknown up another steep climb to the South. \nGive up and return to easier "
                      "territory by heading North"),

    'mountain_east': Room("It's no easy feat to top one of these giants. Enjoy the view!",
                          "Really only one way down from here. \nHead West"),

    'clearing': Room("An opening in the forest reveals a heard of elk grazing.",
                     "The trail seems to disappear here. \nBetter stick to the trail and turn back South"),

    'dense_forest': Room("The forest is so thick here it's dark.",
                         "I becomes too dense to cary on. \nLooks like turning North is the only option"),

    'cave': Room("Hard to say how far back this cave goes. It's pretty dark.",
                 "To climb back down, head to the East."),

    'raging_river': Room("This is colder and deeper than it looked. Faster too.",
                         "Not a good idea.  \nYou're dead."),

    'shallow_crossing': Room("It's much colder than you thought. You loose 10 health.",
                             "Head East to reach a bridge. \nGo West to return to the river bank."),

    'bridge_crossing': Room("Wait, did I just cross a river to find a bridge?! Oh! There's the little dog from the "
                            "rest-stop!",
                            "Walk North to approach the doggo. \nHead back across the bridge to the South."),

    'river_delta': Room("The sun glistens off of the wetlands while songbirds fill the air with sound.",
                        "Head back to the East, unless you have a boat."),

    'stevens_pass': Room("You made it to Steven's Pass! Hope you brought your board!",
                         "Head back North when you've shredded your gnar, brah"),

    'doggo': Room("Finally, the dog that led you into the forest is right here!",
                  "South is the only way to go.")

}

# Connect rooms.
rooms['rest_stop'].to_s = rooms['car']
rooms['rest_stop'].to_n = rooms['forest_trail']

rooms['forest_trail'].to_n = rooms['river_bank']
rooms['forest_trail'].to_e = rooms['trail_east']
rooms['forest_trail'].to_w = rooms['trail_west']
rooms['forest_trail'].to_s = rooms['rest_stop']

rooms['trail_east'].to_n = rooms['kendal_catwalk']
rooms['trail_east'].to_e = rooms['mountain_east']
rooms['trail_east'].to_s = rooms['section_k']
rooms['trail_east'].to_w = rooms['forest_trail']

rooms['trail_west'].to_n = rooms['clearing']
rooms['trail_west'].to_w = rooms['cave']
rooms['trail_west'].to_s = rooms['dense_forest']
rooms['trail_west'].to_e = rooms['forest_trail']

rooms['kendal_catwalk'].to_s = rooms['trail_east']

rooms['section_k'].to_n = rooms['trail_east']
rooms['section_k'].to_s = rooms['stevens_pass']

rooms['stevens_pass'].to_n = rooms['section_k']

rooms['mountain_east'].to_w = rooms['trail_east']

rooms['clearing'].to_s = rooms['trail_west']

rooms['dense_forest'].to_n = rooms['trail_west']

rooms['cave'].to_e = rooms['trail_west']
# Turn out the lights.
rooms['cave'].light = False

rooms['river_bank'].to_n = rooms['raging_river']
rooms['river_bank'].to_s = rooms['forest_trail']
rooms['river_bank'].to_e = rooms['shallow_crossing']
rooms['river_bank'].to_w = rooms['river_delta']

rooms['shallow_crossing'].to_w = rooms['river_bank']
rooms['shallow_crossing'].to_e = rooms['bridge_crossing']

rooms['river_delta'].to_e = rooms['river_bank']

rooms['doggo'].to_s = rooms['bridge_crossing']
rooms['bridge_crossing'].to_n = rooms['doggo']

# Add items.
flashlight = Item('flashlight',
                  'A handy tool to light your way.',
                  weight=5)
flashlight.is_light = True
rooms['rest_stop'].items_[flashlight.name] = flashlight

# Hide an item in a box in the dark in a cave.
# Make a Container.
black_lock_box = Container('black_lock_box',
                           'A sturdy, locked box. It is black',
                           weight=50)

# And something to put in it.
sling_shot = SlingShot('sling_shot',
                       'Launches a small stone at high speeds. Pretty accurate, too.',
                       weight=5)

# Put the item in the box.
black_lock_box.items_[sling_shot.name] = sling_shot

# Lock the box.
black_lock_box.locked = True

# Be sure to make a key.
black_key = Item('black_key',
                 'A black key. Must go to something.',
                 weight=1)

# And fit the key to the box.
black_lock_box.key = black_key

# Hide box and key.
rooms['cave'].items_[black_lock_box.name] = black_lock_box
rooms['dense_forest'].items_[black_key.name] = black_key

# Do the same with at red box.
red_lock_box = Container('red_lock_box',
                         'A sturdy locked box. It is red.',
                         weight=50)
red_key = Item('red_key',
               'A small, red key. Must go to something.',
               weight=1)
red_lock_box.key = red_key
dog_treats = Item('dog_treats',
                  'These will make any doggo your friendo.',
                  weight=2)
red_lock_box.items_[dog_treats.name] = dog_treats
rooms['stevens_pass'].items_[red_key.name] = red_key
rooms['river_delta'].items_[red_lock_box.name] = red_lock_box

pebbles = Pebbles('pebbles',
                  'Small round stones',
                  weight=2)
rooms['clearing'].items_[pebbles.name] = pebbles

berry1 = Berries('huckleberries',
                 'Purple berries bursting with flavor')
rooms['trail_west'].items_[berry1.name] = berry1

berry2 = Berries('blue_berries',
                 'Blue berries bursting with flavor')

rooms['kendal_catwalk'].items_[berry2.name] = berry2

berry3 = Berries('black_berries',
                 'Black berries bursting with flavor')

rooms['river_delta'].items_[berry3.name] = berry3
