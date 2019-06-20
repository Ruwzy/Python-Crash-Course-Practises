sandwich_orders = ["pastrami", "vege", "fish", "chicken", "pastrami", "beef", "pork", "pastrami"]
finished_sandwiches = []

print("The pastrami has been sold out!")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made you a " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nThere are all the sandwiches: ")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())