fav_nums = {
    "Kathy": ["23", "112"],
    "Yankey": ["22", "545"],
    "Ben": ["23", "88"], 
    "Carol": ["24", "244"],
    "Tina": ["111", "2354", "221"],
    }

for people, numbers in fav_nums.items():
    print(people + " loves the number: ")
    for number in numbers:
        print("\t" + number)