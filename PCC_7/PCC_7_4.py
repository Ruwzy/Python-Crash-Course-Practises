cus_toppings = "Please enter the toppings you wanna add in your pizza: "
cus_toppings += "\n(Enter 'quit' to finish your input): "

message = ""
active = True
while active:
    message = input(cus_toppings)

    if message == "quit":
        active = False
        break
    else:
        print("Now we know you want: " + message)