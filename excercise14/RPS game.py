import random

def main():
    opening_message()
    letter_options = ["R", "P", "S"]

#convert this to a int random number by assigning 0,1,2 and using the random.range function
    #assign the number back to the letters?

    while True:
        user_input = input("To compete against the computer, Enter R,P,S to play...")
        computer_input = random.choice(letter_options)

        if user_input.upper() == "R" or user_input.upper() == "P" or user_input.upper() == "S":
            ask_computer_result(user_input)
            print("User has entered" + " ", end="")
            explain_letters(computer_input)
            print("Computer has entered" + " ", end="")
        else:
            same_error()
# code is wrong line 13 and 16

#First message displayed when the game starts

def opening_message():
    print("Come and play the game. Rock, Paper, Scissors!")

#not sure I need this code
def input_letters():
    letters = input("To compete against the computer, Enter R,P,S to play...")


#This functions converts the value of R,P,S
def explain_letters(chosen):
    if chosen.upper() == "R":
        print("Rock")
    elif chosen.upper() == "P":
        print("Paper")
    elif chosen.upper() == "S":
        print("Scissors")


#Loop to compare results between user and computer
def ask_computer_result(user, computer):
    if user.upper() == "R" and computer.upper() == "S":
        print("USER WINS!")
    elif user.upper() == "P" and computer.upper() == "R":
        print("USER WINS!")
    elif user.upper() == "S" and computer.upper() == "P":
        print("USER WINS!")
    elif user.upper() == "S" and computer.upper() == "P":
        print("COMPUTER WINS!")
    elif user.upper() == "R" and computer.upper() == "P":
        print("COMPUTER WINS!")
    elif user.upper() == "P" and computer.upper() == "S":
        print("COMPUTER WINS!")
    else:
        print("Draw!")


# if wrong letter is inputted
def same_error():
    print("Invalid, please type R,P,S...")

main()
#call back to main function

