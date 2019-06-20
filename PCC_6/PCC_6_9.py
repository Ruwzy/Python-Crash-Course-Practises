favourite_places = {
    "Jack": ["CQ", "CD", "GD"],
    "Dora": ["BJ", "SZ", "SH"],
    "Cici": ["HLJ", "CQ"],
    }

for people, places in favourite_places.items():
    print(people + "'s favourite places are: ")
    for place in places:
        print("\t" + place.lower())