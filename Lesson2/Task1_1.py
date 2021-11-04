# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не завершается,
# а запрашивает новые данные для вычислений. Завершение программы должно выполняться при вводе символа
# '0' в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '', '/'),
# программа должна сообщать об ошибке и снова запрашивать знак операции.
# Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.

x, y, sign = [
    x for x in input('Enter 2 number and sign (x y sign): ').split()
]
while True:
    try:
        x, y, sign = [
            x for x in input('Enter 2 number and operand (x y sign): ').split()
        ]

    except ValueError:
        print('Change Enter')
        continue
    x = float(x)
    y = float(y)
    if str(sign) == '0':
        break
    elif str(sign) == '+':
        print(x + y)
    elif str(sign) == '*':
        print(x * y)
    elif str(sign) == '-':
        print(x - y)
    elif str(sign) == '/' and y != 0:
        print(x / y)
    else:
        print('ZeroDivisionError')
