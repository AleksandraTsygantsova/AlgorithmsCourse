# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random
array = [random.randint(0, 100) for i in range(10)]
min = array[0]
max = 0
idx_min = 0
idx_max = 0

for i, item in enumerate(array):
    if item <= min:
        min = item
        idx_min = i
    elif item >= max:
        max = item
        idx_max = i

new_array = array.copy()
new_array[idx_min], new_array[idx_max] = new_array[idx_max], new_array[idx_min]

print(f'Исходный массив случайных элементов: {array}')
print(f'Максимальное число в массиве: {max}, минимальное число в массиве: {min}')
print(f'Новый массив: {new_array}')
