# 8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

x, y, z = [
    float(x) for x in input('Введите три числа (x y z): ').split()
]

if y < x < z or z < x < y:
    print(f'Среднее: {x}')
elif x < y < z or z < y< x:
    print(f'Среднее: {y}')
else:
    print(f'Среднее: {z}')