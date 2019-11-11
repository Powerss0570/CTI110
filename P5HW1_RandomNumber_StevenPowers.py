#Random Number Guessing Game
#11/10/2019
#CTI-110-0007 P5HW1 - Random Number
#Steven Powers

#This is a guess the number game.

def main():
    """ main function does the menu """
    go_again = 'y'
    while (go_again == 'y'):
        print("Choose an option")
        print("1. Random Number Guessing game")
        print("2. Exit")
        option = int(input('Enter the number of your choice '))
        if option == 1:
            game()
        elif option == 2:
            go_again = 'n'
            print("Exiting")
        else:
            print("Not a valid option")

def game():
    import random
    #stores random number between 1 and 100 in a variable called randomNumber
    randomNumber = random.randint(1,100)

    #gets a number guess from user. Stores variable in guess
    guess = int(input("Enter a number between 1 and 100: "))

    #while loops looking for number before it will print the guess it message
    while randomNumber != guess:

        #if the guessed number is less than the random number display hint.
        #get new guessed number.
        if guess < randomNumber:
            print ("Hint: Guess is to low! Try Again.")
            guess = int(input("Enter a number between 1 and 100: "))
        #else if guessed number is greater than the random number display hit
        #get new guessed number.
        elif guess > randomNumber:
            print("Hint: Guess is to high! Try Again.")
            guess = int(input("Enter a number between 1 and 100: "))

    #once randomNumber does equal guess then it will exit
    #while loop and display this message
    print("You guess it. Good Job!")

# Call the main function
main()
