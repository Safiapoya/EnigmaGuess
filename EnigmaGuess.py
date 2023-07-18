import random

game = input("Embark on the EnigmaGuess challenge: Can  you guess the number?\nIf you yes,"
             " click Enter.")
level1 = "Easy"
level2 = "Intermediate"
level3 = "Advanced"
level4 = "Legendary"
print("So you accept to challenge yourself!\nHere we have four different levels:\n"
      "{}: You will guess the number within range 1 to 10.\n"
      "{}: You will guess the number within range 1 to 100.\n"
      "{}: You will guess the number within range 1 to 500.\n"
      "{}: You will guess the number within range 1 to 1000.\n".format(level1,level2,level3,level4))
level = input("Enter your desired level: ").casefold()

if level == level1.casefold():
    highest_val = 10
    answer = random.randint(1, highest_val)
    guesses_left = 3
    print("Guess from 1 to 10")
    while guesses_left > 0:
        easy_guess = int(input("You can only have {} guess!: ".format(guesses_left)))
        if easy_guess == answer:
            print("Congratulations! You guessed the correct number!")
            break
        else:
            if easy_guess > answer:
                print("Guess lower!")
            else:
                print("guess higher!")

        guesses_left -=1

    if guesses_left == 0:
        print("Out of the guesses! The correct answer was {}.".format(answer))

elif level == level2.casefold():
    highest_val = 100
    answer = random.randint(1, highest_val)
    guesses_left = 7
    print("Guess from 1 to 100")
    while guesses_left > 0:
        med_guess = int(input("Trust your instincts, you can only have {} guess!: ".format(guesses_left)))
        if med_guess == answer:
            print("Congratulations! You guessed the correct number!")
            break
        else:
            if med_guess > answer:
                print("Guess lower!")
            else:
                print("guess higher!")


        guesses_left -=1

    if guesses_left == 0:
        print("Out of the guesses! The correct answer was {}.".format(answer))

elif level == level3.casefold():
    highest_val = 500
    answer = random.randint(1, highest_val)
    guesses_left = 9
    print("Bravo, Welcome to the Advanced level of EnigmaGuess!\nGuess from 1 to 500")
    while guesses_left > 0:
        hard_guess = int(input("you can only have {} guess!: ".format(guesses_left)))
        if hard_guess == answer:
            print("Congratulations! You guessed the correct number!")
            break
        else:
            if hard_guess > answer:
                print("Guess lower!")
            else:
                print("guess higher!")

        guesses_left -=1

    if guesses_left == 0:
        print("Out of the guesses! The correct answer was {}.".format(answer))

elif level == level4.casefold():
    highest_val = 1000
    answer = random.randint(1, highest_val)
    guesses_left = 10
    print("By selecting the Legendary level, "
          "you want to prove yourself as an exceptional player!\nGuess from 1 to 1000")
    while guesses_left > 0:
        leg_guess = int(input("you can only have {} guess!: ".format(guesses_left)))
        if leg_guess == answer:
            print("Congratulations! You guessed the correct number!")
            break
        else:
            if leg_guess > answer:
                print("Guess lower!")
            else:
                print("guess higher!")

        guesses_left -=1

    if guesses_left == 0:
        print("Out of the guesses! The correct answer was {}.".format(answer))

else:
    print("Please select you level!")

