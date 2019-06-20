sandwich_orders = ["vege", "fish", "chicken", "beef", "pork"]
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made you a " + current_sandwich.lower() + "sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nThere are all the sandwiches: ")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())
