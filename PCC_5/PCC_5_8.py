user_lists = ["Apple", "Ben", "Cherry", "Jemmy", "Admin"]

for user in user_lists:
    if user == "Admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello, " + str(user) + ", nice to see you today.")