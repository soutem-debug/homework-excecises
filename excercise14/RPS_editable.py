import random


def main():
    welcome_message()


    while True:
        user_turn = int(input("Chose 0 for Rock, 1 for Paper or 2 for Scissors:" + " "))
        computer_turn = random.randrange(0, 3)

        if user_turn != 0 and user_turn != 1 and user_turn != 2:
            print("User has chosen:" + " " + " ")
            words(user_turn)
            print("Computer has chosen:" + " " + " ")
            words(computer_turn)
            ask_computer_result(user_turn, computer_turn)
        else:
            same_error()


def welcome_message():
    print("Welcome to a game of Rock, Paper, Scissors!:" + " " + " ")
    input()


def words(chosen):
    if chosen == 0:
        print("Rock")
    elif chosen == 1:
        print("Paper")
    elif chosen == 2:
        print("Scissors")


def ask_computer_result(user, computer):
    if user == computer:
        print("It is a draw")
    if user == 0 and computer == 2:
        print("User chose Rock and wins the round")
    if user == 1 and computer == 0:
        print("User chose Paper and wins the round")
    if user == 2 and computer == 1:
        print("User chose Scissors and wins this round")
    if user == 0 and computer == 1:
        print("Computer chose Paper and wins the round")
    if user == 2 and computer == 0:
        print("Computer chose Rock and wins the round")
    if user == 1 and computer == 2:
        print("Computer chose Scissors and wins this round")


def same_error():
    int(print("Invalid entry, please type 0,1,2..."))


main()
