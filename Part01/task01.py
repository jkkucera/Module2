number1 = float(input('Enter first number: '))
number2 = float(input('Enter second number: '))
number3 = float(input('Enter third number: '))
operation = input('Select Operation (sum/product): ').strip().lower()

if operation == 'sum':
    print(number1+number2+number3)
elif operation == 'product':
    print(number1*number2*number3)
else: 
    print('Invalid operation')