import getpass

print("Enter PIN to continue...")
supplied_pin = input("Enter your PIN: ")


def verify_pin(pin):
    if pin == '6700':
        return True
    else:
        return False


def log_in():
    count = 0
    while count < 4:
        if verify_pin(supplied_pin):
            print("PIN correct")
            return True
        else:
            print("PIN invalid. 3 tries max")
            count += 1
            return False
    while False:

    if count > 4:
        print("No more tries. Please contact bank to unblock")

def start_menu() -> object:
    count = 1
    while count < 4:
        if log_in():
            print(" PIN invalid. Try again")
    count = 2
    while count < 4:
        if log_in():
            print("PIN invalid. Second attempt")
start_menu()





