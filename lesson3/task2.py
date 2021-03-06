#2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# второй массив надо заполнить значениями 0, 3, 4, 5 (помните, что индексация начинается с нуля),
# т. к. именно в этих позициях первого массива стоят четные числа.

import random
array = [random.randint(0, 100) for i in range(10)]
new_array = []

for i, item in enumerate(array):
    if item % 2 == 0:
        new_array.append(i)
    else:
        continue

print(f'Исходный случайнный массив: {array}')
print(f'Индексы четных элементов первого массива: {new_array}')