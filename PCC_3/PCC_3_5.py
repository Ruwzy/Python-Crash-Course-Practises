inv_people = ["Beauvoir", "ZeDong Mao", "Enlai Zhou", "Frank"]
print("Hi, " + inv_people[0] + ", please come to dinner.")
print("Hi, " + inv_people[1] + ", please come to dinner.")
print("Hi, " + inv_people[2] + ", please come to dinner.")
print("Hi, " + inv_people[3] + ", please come to dinner.")
print(inv_people[3] + " cannot come to our dinner.")

del inv_people[3]
inv_people.insert(3, "Ruby")
print("Hi, " + inv_people[0] + ", please come to dinner.")
print("Hi, " + inv_people[1] + ", please come to dinner.")
print("Hi, " + inv_people[2] + ", please come to dinner.")
print("Hi, " + inv_people[3] + ", please come to dinner.")
