num1 = float(input('Enter first digit: '))
num2 = float(input('Enter second digit: '))
num3 = float(input('Enter third digit: '))
numbers = [num1, num2, num3]
operation = input('Select Operation (max/min/average): ').strip().lower()

operations = {
    'max': max(numbers),
    'min': min(numbers),
    'average': sum(numbers)/len(numbers)
}

if operation in operations:
    print(f'{operation} is',operations[operation])
else:
    print('Invalid operation')