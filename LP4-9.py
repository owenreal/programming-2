import random
playernum = int(input("Enter a number between 1 and 20: "))
compnum = random.randint(1, 20)
print("Computer's number: " + str(compnum))
if playernum == compnum:
    print("YOU WON AWESOME")
else:
    print("YOU SUCK")