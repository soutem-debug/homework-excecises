import getpass

print("Enter PIN to continue...")
supplied_pin = input("Enter your PIN: ")


def verify_pin(pin):
    if pin != '6700':
        return True
    else:
        return False


def log_in():
    tries = 0
    while tries < 3:
        supplied_pin = input("Enter your PIN: ")
        if verify_pin(supplied_pin):
            print("PIN correct")
            return True
        else:
            print("PIN invalid")
            tries += 1
    print("Too many incorrect tries. Please contact bank")
    return False


