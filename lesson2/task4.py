# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

qty = int(input('Введите количество элементов для вычисления: '))
sum = 0
num = -2
elements = ''

for i in range(qty):
    num = num / (-2)
    sum = sum + num
    elements = elements + f'{num}, '


print(f'Сумма {qty} элементов ряда [{elements}...] равна {sum}')
