number1 = int(input("Enter the start of the range: "))
number2 = int(input("Enter the end of the range: "))

while number1 <= number2:

    remainder = number1%7
    if remainder == 0:
        print(number1)

    number1 += 1

