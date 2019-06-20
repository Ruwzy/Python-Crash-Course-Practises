dream_places = {}

running_active = True

while running_active:
    user_name = input("\nMay I have your name?")
    user_place = input("\nIf you could visit one place in the world, shere would you go?")

    dream_places[user_name] = user_place

    repeat = input("\nIs there anyone more want to answer the question? (Use Y/N to answer)")
    if repeat.upper() == "N":
        running_active = False

print("\nThe result:")
for user_name, user_place in dream_places.items():
    print(user_name + "'s dream place is " + user_place + ".")
