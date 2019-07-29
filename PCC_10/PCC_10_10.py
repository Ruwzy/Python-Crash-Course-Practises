filename = "testword.txt"

try:
    with open(filename, 'rb') as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print("You don't have such a txt.")
else:
    contents = contents.lower()
    the_num = contents.count('the')
    print("The txt has " + str(the_num) + "'the's.")
