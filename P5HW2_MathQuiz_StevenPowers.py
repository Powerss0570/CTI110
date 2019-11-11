#Math Quiz
#11/11/2019
#CTI-110-0007 P5HW2 - Math Quiz
#Steven Powers

def main():

    keep_going = "y"

    while (keep_going == "y"):
        print ("Main Menu")
        print("---------------")
        print("1) Add Random Numbers")
        print("2) Subtract Random Numbers")
        print("3) Exit")

        choice = int(input("Choose your option:"))

        if choice == 1:
            add()
        elif choice == 2:
            sub()
        elif choice == 3:
            print ("See You Next Time")
            exit()

def add():
    import random

    number1 = random.randint(1,100)
    number2 = random.randint(1, 100)

    answer = int(input("What is  " + str(number1) + "+" + str(number2) + "  ?"))
    correct_answer = number1 + number2
    if answer == correct_answer:
        print("Congratulations!")

    else:
        print ("Incorrect. The correct answer is",  correct_answer)


def sub():
    import random
    import math
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)

    answer = int(input("What is   " + str(number1) + "-" + str(number2) + "  ?"))
    correct_answer = number1 - number2
    if answer == correct_answer:
        print("Congratulations!")

    else:
        print ("Incorrect. The correct answer is", correct_answer)

main()
