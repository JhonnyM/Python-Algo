states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {}
stations['kone'] = set(["id", "nv", "ut"])
stations['ktwo'] = set(["wa", "id", "mt"])
stations['kthree'] = set(["or", "nv", "ca"])
stations['kfour'] = set(["nv", "ut"])
stations['kfive'] = set(["ca", "az"])

final_stations = set()

while states_needed: 
    best_station = None
    states_covered = set() # a set is a list, except they dont accept duplicates
    for station, states in stations.items():
        covered = states_needed & states# this is called a set intersection, you can do funny things with it : union, intersection and difference
            # union sets means combine both sets
            # intersection finds  the items  that show up  in both sets.
            # difference means substract the items in one set from the items in the other set.
        if len(covered) > len(states_covered): 
            best_station = station
            states_covered = covered
states_needed -=  states_covered
final_stations.add(best_station)

print(final_stations) 