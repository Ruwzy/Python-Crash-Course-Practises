print("Please enter 'q' for quit.")

while True:
    user_name = input("Please enter your username or 'q' for quit: ")
    if user_name != 'q':
        print("Hello, nice to meet you today.")

        filename = "guest_book.txt"
        with open(filename, 'a') as file_object:
            file_object.write(user_name)
            file_object.write("\n")
    else:
        break

