filename = "testword.txt"

try:
    with open(filename, 'rb') as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print("You don't have such a txt.")
else:
    the_num = contents.lower().split()
    len_num = len(the_num)
    print("The txt has " + str(len_num) + " words.")