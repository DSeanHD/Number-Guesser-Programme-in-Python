import random

answer = random.randrange(1, 101)
chance = 0
print("You only have 5 chances")

while chance < 5:
    guess = int(input("Guess a number from 1 to 100 "))
    if guess == answer:
        print("You guessed it!!")
        break
    if guess > answer:
        print("Go lower")
    elif guess < answer:
        print("Go higher")

    chance += 1

    if chance == 5:
        print("Game Over")
        print("The number was", answer)
        break