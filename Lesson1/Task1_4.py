# 4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

x, y = [
    str(x) for x in input('Введите 2 буквы (x y): ').split()
]

letter = 'abcdifghijklmnopqrstuvwxyz'
number = list(range(26))
dic = dict(zip(number, letter))
number1 = [k for k, v in dic.items() if v == x]
number2 = [k for k, v in dic.items() if v == y]
number3 = abs(number1[0]- number2[0])
print(f'Слово x стоит на {number1[0]}')
print(f'Слово y стоит на {number2[0]}')
print(f'Между ними {number3} букв')
