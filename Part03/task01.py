start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

for number in range(start_range, end_range + 1):
    if number > 1: 
        for divisor in range(2, int(number ** 0.5) + 1):
            remainder = number % divisor
            if remainder == 0:
                break
        else:
            print(number)