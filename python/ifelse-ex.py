import random

rnum = (random.randrange(10,99))
gnum = int(input("Enter 2 digit guessed number: "))
if rnum == gnum:
    print("You guessed right!!")
else:
    if gnum < rnum:
        print("guessed number is low from random")
    else:
        print("guessed number is high from random")
        
print(gnum)
print(rnum)
