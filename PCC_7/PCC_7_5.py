question = "May I have your age for pricing the ticket?"
question += "\n(Enter 'quit' to end the input): "

message = ""

active = True
while active:
    message = input(question)
    if message == "quit":
        active = False
        break
    elif int(message) < 3:
        print("You got a free ticket!")
    elif int(message) >=3 and int(message) <= 12:
        print("Your ticket's price is $10.")
    else:
        print("Your ticket's price is $15.")
    
