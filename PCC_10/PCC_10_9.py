try:
    with open('cats.txt') as file_object:
        contents = file_object.read()
except FileNotFoundError:
    pass
else:
    print(contents)