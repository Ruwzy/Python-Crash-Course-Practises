eat_num = "Please tell me how many people will come to eat: \n"
num = input(eat_num)
num = int(num)

if num >= 8:
    print("There is no such a big room for you, sorry.")
else:
    print("Welcome here, we got enough table for you.")
