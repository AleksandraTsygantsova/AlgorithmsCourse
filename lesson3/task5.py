# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

import random
array = [random.randint(-100, 100) for i in range(20)]

neg_array = []
for i in array:
    if i < 0:
        neg_array.append(i)

max_neg = neg_array[0]
for i in neg_array:
    if i < max_neg:
        max_neg = i

max_neg_idx = neg_array.index(max_neg)

print(f'Исходный массив случайных чисел: {array}')
print(f'Максимальный отрицательный элемент: {max_neg}, его индекс: {max_neg_idx}')
