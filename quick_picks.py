import random

numbers_per_line = 6
minimum = 1
maximum = 45


def main():


    number_of_quick_picks = int(input("How many numbers do you want? "))
    while number_of_quick_picks <0:
        print("Please enter a valid number: ")
        number_of_quick_picks = int(input("How many numbers do you want? "))
    for i in range(number_of_quick_picks):
        quick_pick = []
        for display in range(numbers_per_line):
            number = random.randint(minimum, maximum)
            while number in quick_pick:
                number = random.randint(minimum, maximum)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))


main()