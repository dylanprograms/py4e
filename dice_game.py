import random
#takes an input nod (number of dice)
#prints the result of rolling nod
rolls = []
def roll_dice(nod):
    score = 0
    repeat = True
    while repeat:
        guess = int(input("Guess a number between 1 and 6. "))
        if guess in range(1,7):
            print("Your guess is " + str(guess))
            for i in range(nod):
                roll = random.randint(1,6)
                rolls.append(roll)
                print(roll)
                if guess == roll:
                    print("That's a match!")
                    score += 1
            user_input = input("Roll again? y/n? ").lower()
            if user_input == "n":
                repeat = False
    print("Game Over.")
    if score > 1 or score < 1:
        print("You scored " + str(score) +" matches!")
    else: 
        print("You scored " + str(score) + " match!")


roll_dice(6)
