try:
    with open('cats.txt') as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print("There's no such file exits.")
else:
    print(contents)

