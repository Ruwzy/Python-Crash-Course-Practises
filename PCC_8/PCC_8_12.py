def sandwich_ingredients(*ingredients):
    print("\nThe ingredients you wanna put in the sandwich: ")
    for ingredient in ingredients:
        print("-" + ingredient)

sandwich_ingredients("beef")
sandwich_ingredients("eggs", "tomato")
sandwich_ingredients("pork", "egg", "chicken")