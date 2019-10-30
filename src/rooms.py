from room import Room

# Declare rooms in rooms dict.
# TODO: Add items to rooms.
rooms = {
    'rest_stop': Room("A North Cascades Hwy rest-stop.",
                      """North of you, a little dog barks and dashes down a forest trail.
To the South, your warm car and the open road."""),

    'car': Room("You head down the road, wondering what could have been.",
                "An 18 wheeler crushes you. Look both ways before entering traffic."),

    'forest_trail': Room("The trail opens to snow capped peaks and a lush valley.",
                         """To the North, a wild river runs
Other trails lead to the East and West"""),

    'river_bank': Room("The clear, cold river rushes at your feet.",
                       """Attempt to ford the river by heading North
Head upstream to the East
Move toward the Puget Sound by heading downstream, to the West"""),

    'trail_east': Room("A massive peak looms above.",
                       """Climb the peak by continuing East
Head North along Kendal Catwalk
To the South is the difficult Section K of the Pacific Crest Trail"""),

    'trail_west': Room("The trail forks at a granite outcropping.",
                       """A short climb East looks like the entrance to a cave
The trail continues both North and South"""),

    'kendal_catwalk': Room("A narrow walkway juts out from the shear cliff, to fall hear is certain death.",
                           """An avalanche has blocked your path
You must return to the South"""),

    'section_k': Room("This difficult trail seems to go on forever.",
                      """Continue into the unknown up another steep climb to the South
Give up and return to easier territory by heading North"""),

    'mountain_east': Room("It's no easy feat to top one of these giants. Enjoy the view!",
                          """Really only one way down from here
Head West"""),

    'clearing': Room("An opening in the forest reveals a heard of elk grazing.",
                     """The trail seems to disappear here
Better stick to the trail and turn back South"""),

    'dense_forest': Room("The forest is so thick here it's dark.",
                         """I becomes too dense to cary on
Looks like turning North is the only option"""),

    'cave': Room("Hard to say how far back this goes. It's pretty dark.",
                 """Head West to enter the cave
Climb back down to the East otherwise"""),

    'raging_river': Room("This is colder and deeper than it looked. Faster too.",
                         """Not a good idea. 
You're dead."""),

    'shallow_crossing': Room("It's much colder than you thought. You loose 10 health.",
                             """"""),

    'bridge_crossing': Room("Well worth walking a little further to find this! And there's the little dog from the "
                            "rest-stop!",
                            """Walk North to approach the doggo
Head back across the bridge to the South"""),

    'river_delta': Room("The sun glistens off of the wetlands while songbirds fill the air with sound.",
                        """Head back to the East"""),

    'stevens_pass': Room("You made it to Steven's Pass! Hope you brought your board!",
                         """Head back North when you've shredded your gnar, brah""")

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

rooms['river_bank'].to_n = rooms['raging_river']
rooms['river_bank'].to_s = rooms['forest_trail']
rooms['river_bank'].to_e = rooms['shallow_crossing']
rooms['river_bank'].to_w = rooms['river_delta']

rooms['shallow_crossing'].to_w = rooms['river_bank']
rooms['shallow_crossing'].to_e = rooms['bridge_crossing']

rooms['river_delta'].to_e = rooms['river_bank']
