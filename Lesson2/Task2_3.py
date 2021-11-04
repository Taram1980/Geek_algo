# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

number = input('Enter number: ')
number = int(number)

# number = 123456564656
number1 = 0
mul = len(str(number)) - 1
number1 = 0
while mul != 0:
    mul = len(str(number)) -1
    number1 += number%10 * 10**mul
    number = number//10

print(number1, number)
