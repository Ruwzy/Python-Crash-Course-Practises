river_dic = {"Yanzi River": "China", "Missisipi": "United States", "Nile": "Egypt"}

for river, nation in river_dic.items():
    print("The " + river + " runs through " + nation)

for river in river_dic.keys():
    print("The river's name is " + river)

for river in river_dic:
    print("The river's name is " + river)

for nation in river_dic.values():
    print("The nation is: " + nation)