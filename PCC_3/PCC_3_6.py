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

print("Now we have bigger room for more people to take the dinner!")
inv_people.insert(0, "Jackie")
inv_people.insert(2, "Zetian Wu")
inv_people.append("Mum")
print(inv_people)
print("Hi, " + inv_people[0] + ", please come to dinner.")
print("Hi, " + inv_people[1] + ", please come to dinner.")
print("Hi, " + inv_people[2] + ", please come to dinner.")
print("Hi, " + inv_people[3] + ", please come to dinner.")
print("Hi, " + inv_people[4] + ", please come to dinner.")
print("Hi, " + inv_people[5] + ", please come to dinner.")
print("Hi, " + inv_people[6] + ", please come to dinner.")