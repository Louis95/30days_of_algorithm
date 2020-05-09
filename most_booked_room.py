import collections

def most_booked_room(rooms):
    # create a list of only booked rooms
    booked_rooms = [room for room in rooms if room[0] == "+"]
    # count the number of times each room is booked
    count = collections.Counter(booked_rooms)
    most_common = sorted(count.items(), key=lambda pair: (-pair[1], pair[0])) 

    # frq = count.most_common()
    # print(frq)
    return most_common[0][0]

    # for room,freq in most_common[:3]:
    #     return room

print(most_booked_room(["-1A", "+3E", "+1A", "+3E", "+4F", "+1A","+4F", "-3E", "+3E", "-4F"]))

