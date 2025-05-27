"""
Khansole Academy - Three in a row is a program that randomly generates a simple addition problem for the user,
reads in the answer from the user, and then checks to see if they got it right or wrong. 
When the user has solved 3 additions correct in a row, the program congratulates
the user and ends.
"""

import random

def random_number():
    """
    This function returns a random number from 1 to 100
    using the random.randint function.
    """
    return random.randint(1, 100)

def get_user_input():
    """
    """
    while True:
        print("Please enter a number")
        input_sum = input("Your answer: ") # The users sum of the addition
        if input_sum.isnumeric():
            break
    return int(input_sum)

def main():
    """
    Generate two random numbers and perform a addition.
    The user will be ask what the total of the addition is.
    The input sum will be evaluated, and prints if its right or wrong.
    If it's right the value correct will be +1. 
    If its wrong the correct value will fall back to 0.
    If the value correct = 3 the program ends.
    """
    number_correct = 0 # The variable correct stores the number of correct responses that the user enters in a row.
    print("----------------------------------")
    print("Khansole Academy - Three in a row")
    print("If you want to quit press 0")
    print("----------------------------------")
    while number_correct < 3: # Program ends when user answers 3 questions correctly in a row.
        rand_num1 = random_number() # Random number 1
        rand_num2 = random_number() # Random number 2
        total = rand_num1 + rand_num2 # The total of the addition of rand_num1 and rand_num2
        print(f"What is {rand_num1} + {rand_num2}?")
        input_sum = get_user_input()
        if input_sum == 0: # The program ends if the user enters 0.
            print("Goodbye, see you next time. 👋")
            break
        elif input_sum == total:
            number_correct += 1 
            if number_correct == 3:
                print("Congratulations! You have three in a row! 🎉🎉🎉")
            else:
                print(f"Correct! You have now {number_correct} in a row! 👍")
        else:
            number_correct = 0
            print(f"Incorrect! The expected answer is {total}")

# necessary boilerplate to start execution
if __name__ == '__main__':
    main()
