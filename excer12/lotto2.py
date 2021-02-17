

import random

main_numbers = []

main_numbers_count = 0

while main_numbers_count < 6:
    number = random.randrange(1, 50)

    if number not in main_numbers:
        main_numbers.append(number)
        main_numbers_count += 1

main_numbers.sort()

print("The Lottery numbers today are: ", main_numbers)

