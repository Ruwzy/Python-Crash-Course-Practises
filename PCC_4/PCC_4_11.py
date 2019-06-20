fav_pizzas = ["tomato", "cheese", "bacon"]
friend_pizzas = fav_pizzas[:]
fav_pizzas.append("meatball")
friend_pizzas.append("carrot")

print("My favourite pizzas are:")
for pizza in fav_pizzas:
    print(pizza)

print("My friend's favourite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
    