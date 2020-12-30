# 4. Определить, какое число в массиве встречается чаще всего.
import random

array = [random.randint(0, 10) for i in range(15)]
array_set = list(set(array))
result = {}

for i in array_set:
    result[i] = 0

for i in array:
    result[i] += 1

max_count = 0
max_item = ''

for key, value in result.items():
    if value >= max_count:
        max_item = key
        max_count = value

print(f'Исходный случайный массив: {array}')
print(f'Число {max_item} встречается в массиве {max_count} раз')
