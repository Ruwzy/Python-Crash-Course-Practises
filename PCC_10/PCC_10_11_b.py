import json

filename = "cus_num.json"
with open(filename) as f_obj:
    cus_num = json.load(f_obj)

print("I know your favourite number! It's " + str(cus_num))