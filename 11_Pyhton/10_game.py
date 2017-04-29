## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# Generate the 3 digit random number
import random


def generate_code():
    """
    Generate a 3 unique digit number
    """
    digits = [str(num) for num in range(10)]
    random.shuffle(digits)
    solution = digits[:3]
    print(solution)
    return solution


def get_user_guess():
    """
    Get user guess
    """
    return list(input("What is your guess?\n"))


def check_user_guess(user_guess, game_code):
    """
    Check if the user guess is correct or get the clues if not
    """
    if user_guess == game_code:
        return "Game Won"

    results = []
    for index, number in enumerate(user_guess):
        if number == game_code[index]:
            results.append("Match")
        elif number in game_code:
            results.append("Close")
    if results == []:
        return ["Nope"]
    else:
        return results


print("Game Starts!")
code = generate_code()
result = []

while result != "Game Won":

    user_guess = get_user_guess()
    result = check_user_guess(user_guess, code)

    print("Here is the result of your guess:")
    if result == "Game Won":
        print("Game Won!!")
    else:
        for clue in result:
            print(clue)
