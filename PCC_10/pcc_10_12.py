import json

filename = "cus_num.json"
try:
    with open(filename) as f_obj:
        cus_num = json.load(f_obj)
except FileNotFoundError:
    cus_num = input("What's your favourite number?")
    with open(filename, 'w') as f_obj:
        json.dump(cus_num, f_obj)
        print("I'll remember that.")
else:
    print("I know your favourite number! It's " + cus_num + ".")
