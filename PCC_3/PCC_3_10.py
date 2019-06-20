nations = ["China", "United States", "United Kingdom", "France", "Japan"]
print(nations[0].title())

nations[0] = "Korea"
print(nations)

nations.append("Iceland")
print(nations)

nations.insert(2, "German")
print(nations)

del_nation = nations.pop(0)
print(nations)

del nations[4]
print(nations)

remove_nation = nations.remove("United States")
print(nations)

nations.reverse()
print(nations)

print(sorted(nations))
print(sorted(nations, reverse = True))

nations.sort()
print(nations)

nations.sort(reverse = True)
print(nations)