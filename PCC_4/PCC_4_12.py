my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]

my_foods.append("bacon")
friend_foods.append("ice cream")

print("My favourite foods are:")
for food in my_foods:
    print(food)

print("My friend's favourite foods are:")
for food in friend_foods:
    print(food)
 