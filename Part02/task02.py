start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

list_numbers = []
list_multiples_seven = []
list_multiples_five = []
list_reversed = []

for number in range(start_range, end_range + 1):
    list_numbers.append(number)
    if number % 7 == 0:
        list_multiples_seven.append(number) 
    if number % 5 == 0:
            list_multiples_five.append(number)

for number in range(end_range, start_range - 1, -1):
    list_reversed.append(number)

print('Full range: ',list_numbers)
print('Reversed range: ',list_reversed)
print('Multiples of 7: ',list_multiples_seven)
print('Count of multiples of 5: ',len(list_multiples_five))


