import random

num_lst = list(range(51))
print(num_lst)


def random_number_gen():
    random.randint(1, 50)
    return random


def generateRandom():
    pass


def generate_lotto_num(lotto_number):
    lotto_number = []

    for currentLottoIndex in range(50):
        randomNumber = generateRandom()
        randomNumber.append(randomNumber)

    return randomNumber


def printLottoNumbers(lottoNumbers):
    for currentLottoIndex in range(len(lottoNumbers)):
        print(lottoNumbers[currentLottoIndex])


def main() -> object:
    number_lotto_numbers = 6
    lotto = []

    lotterynumbers = generateRandom()

    print("The", number_lotto_numbers, "numbers today are: ")

    printLottoNumbers()


main()
