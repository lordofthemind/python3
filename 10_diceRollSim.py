import random

def rocknroll():
    roll = input("Roll the dice? (y/n)")

    while roll.lower() == "y".lower():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print(dice1)
        print(dice2)

        roll = input("Roll the dice? (y/n)")

rocknroll()