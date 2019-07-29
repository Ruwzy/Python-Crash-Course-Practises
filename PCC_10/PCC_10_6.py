try:
    x = input("Enter a number: ")
    x = int(x)
    y = input("Enter another number: ")
    y = int(y)
except ValueError:
    print("You have to enter a number ,not a word.")
else:
    z = x + y
    print("The answer is: " + str(z))
