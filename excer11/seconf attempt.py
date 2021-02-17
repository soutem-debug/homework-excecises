import from getpass

pin = '6700'
number_of_tries = 3

for attempt in range(1, number_of_tries + 1):
    supplied_pin = getpass.getpass("Enter your PIN number: ")
    if supplied_pin == pin:
        print("PIN correct... loading")
        break
    elif attempt is not number_of_tries:
        print(f"PIN not correct, {number_of_tries - attempt} attempts left.")
    else:
        print("No more attempts. Please contact bank")