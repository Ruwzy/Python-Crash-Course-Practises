import json

cus_num = input("Please enter your favourite number: ")

filename = "cus_num.json"
with open(filename, 'w') as f_obj:
    json.dump(cus_num, f_obj)
