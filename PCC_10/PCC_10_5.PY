print("Please answer the question and use 'q' to quit.")

while True:
    reason = input("Why you love programming( use 'q' for quiting: ")
    if reason != "q":
        filename = "reason.txt"
        with open(filename, "a") as file_object:
            file_object.write(reason)
            file_object.write("\n")
    else:
        break

        