# 6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, вывести ответ.

import random

rand_int = random.randint(0, 100)
n = 0
print(rand_int)
while n <= 10:
    try:
        number = input('Enter number from 0 to 100: ')
        number = int(number)
        n += 1
        if number == rand_int:
            print('You gess')
            break
        else:
            if number < rand_int:
                print('You dont gess,  try a bigger number.')
                continue
            else:
                print('You dont gess, try a number smaller.')
                continue
    except ValueError:
        print('Change Enter')

