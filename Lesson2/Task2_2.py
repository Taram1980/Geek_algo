number = input('Enter number (x): ')

even = 0
odd = 0
for numbers in str(number):
    numbers = float(numbers)
    if numbers % 2 == 0:
        even += 1
    else:
        odd += 1
print('Четных: {}, Нечетных: {}'.format(even, odd))