def direction_helper(direction, room, gamer):
    if direction.lower()=='n':
        if room[gamer.current_room].n_to == None:
            print('There is no room to towards that direction')
        else:
            for room_name in room:
                if room_name in room[gamer.current_room].n_to.name.lower() :
                    print(room_name)
                    gamer.current_room = room_name
                    break

    elif direction.lower()== 's':
            for room_name in room:
                if room_name in room[gamer.current_room].s_to.name.lower() :
                    print(room_name)
                    gamer.current_room = room_name
                    break            
    elif direction.lower()== 'w':
            for room_name in room:
                if room_name in room[gamer.current_room].w_to.name.lower() :
                    print(room_name)
                    gamer.current_room = room_name
                    break     

    elif direction.lower()== 'e':
            for room_name in room:
                if room_name in room[gamer.current_room].e_to.name.lower() :
                    print(room_name)
                    gamer.current_room = room_name
                    break     


                