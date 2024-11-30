start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

for i in range(start_range, end_range +1):
    for j in range(start_range, end_range +1):
        result = i * j
        print(f'{i}*{j}=',result,end='\t')
    print('\n')