from random import randint


class Die():

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        ran_num = randint(1, self.sides)
        print(ran_num)


six_dice = Die()
time = 0
while True:
    if time < 10:
        six_dice.roll_die()
        time = time + 1
    else:
        print("You have roll 10 times!")
        break

six_dice = Die(sides=10)
time = 0
while True:
    if time < 10:
        six_dice.roll_die()
        time = time + 1
    else:
        print("You have roll 10 times!")
        break

six_dice = Die(sides=20)
time = 0
while True:
    if time < 10:
        six_dice.roll_die()
        time = time + 1
    else:
        print("You have roll 10 times!")
        break
