user_name = input("Please enter your username: ")

filename = "guest.txt"

with open(filename, 'a') as file_object:
    file_object.write(user_name)

    