def main():
    numbers = []
    for i in range(5):
        number= int(input("Please enter Number {}:".format(i + 1)))
        numbers.append(number)

        print("The first number is:", numbers[0])
        print("The last number is:", numbers[-1])
        print("Smallest number is,", min(numbers))
        print("Largest number is,", max(numbers))
        print("The average number is", sum(numbers) / len(numbers))

main()
