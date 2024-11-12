import random

score = 0
print("Welcome to number guesser. Where you have to guess the correct number to score. You get 3 tries for each game and the number is always between 0 and 9.")


while True:
    guess_count = 0
    number = random.randint(1,9)
    print(number) #For the purpose of testing the game the random number will be printed.

    while guess_count < 3:
        guess = int(input("Please input your guess: "))

        if guess == number:
            score += 1
            guess_count += 1
            print("You guessed correctly. Your current score is " + str(score) + ". And you made " + str(guess_count) + " guesses.")
            break
        elif 0 < guess < number:
            guess_count += 1
            print("Your guess is too low. Try again. You have made " + str(guess_count) + " guesses.")
        elif 10 > guess > number:
            guess_count += 1
            print("Your guess is too high. Try again. You have made " + str(guess_count) + " guesses.")
        else: print("Invalid Input")
    
    replay = input("Would you like to play again (Y/N): ").lower()
    if replay == "n": #Elif can be added incase the input is 'y'.
        break
    
print("Your final score is " + str(score))

