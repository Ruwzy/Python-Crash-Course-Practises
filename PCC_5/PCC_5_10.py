current_users = ["Adam", "Ben", "Cherry", "Dean", "Ed"]
new_users = ["Ed", "Alice", "Cherry", "Claire", "Denny"]

for user in new_users:
    if user in current_users:
        print(str(user) + ", your ID has been taken, choose another one.")
    else:
        print(str(user) + ", you got the luck! The ID hasn't been taken! You can use it.")

