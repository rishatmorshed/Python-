import random

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5
def set_difficulty(level_type):
    if level_type == 'easy':
        return EASY_LEVEL_ATTEMPTS
    elif level_type == 'hard':
        return HARD_LEVEL_ATTEMPTS
    
def check_answer(guessed_num, answer, attempts):
    if guessed_num<answer:
        print("Your guess is too low")
        return attempts-1
    elif guessed_num>answer:
        print("Your guess is too high.")
        return attempts-1
    else:
        print(f"Your guess was right...The answer is {answer}")

def game():
    continue_flag = True
    while continue_flag:
        print("Let me think of a number between 1 to 50.")
        answer = random.randint(1, 50)
        level = input("Choose level of difficulty...Type 'easy' or 'hard': ").lower()
        attempts = set_difficulty(level)
        guessed_num = 0
        while guessed_num != answer:
            print(f"You have {attempts} attemps remaining to guess the number!")
            guessed_num = int(input("Guess a number: "))
            attempts = check_answer(guessed_num, answer, attempts)
            if attempts == 0:
                print(f"You are out of guesses...You lose! The answer was {answer}")
                re_play=input("Press 'y' to play again or 'x' to exit: ")
                if re_play == 'y':
                    game()
                elif re_play == 'x':
                    continue_flag = False
                    print("Bye.. Have a good day!")
                return 
            elif guessed_num != answer:
                print("Guess again")
game()