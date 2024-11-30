start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

for number in range(start_range, end_range + 1):
    if number % 5 == 0 and number % 3 == 0:
        print('Fizz Buzz')
    elif number % 5 == 0:
        print('Buzz')
    elif number % 3 == 0:
        print('Fizz')
    else:
        print(number)


