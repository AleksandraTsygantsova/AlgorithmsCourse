# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел
# в диапазоне от 2 до 9. Примечание: 8 разных ответов.

import random
array = [random.randint(2, 99) for i in range(10)]
result = {'2-ум': [], '3-ем': [], '4-ем': [], '5-ти': [], '6-ти': [], '7-ми': [], '8-ми': [], '9-ти': []}

for i in array:
    if i % 2 == 0:
        result['2-ум'].append(i)
    if i % 3 == 0:
        result['3-ем'].append(i)
    if i % 4 == 0:
        result['4-ем'].append(i)
    if i % 5 == 0:
        result['5-ти'].append(i)
    if i % 6 == 0:
        result['6-ти'].append(i)
    if i % 7 == 0:
        result['7-ми'].append(i)
    if i % 8 == 0:
        result['8-ми'].append(i)
    if i % 9 == 0:
        result['9-ти'].append(i)

print(f'Исходный массив случайных чисел: {array}')
for key, value in result.items():
    print(f'Количество чисел кратных {key}: {len(value)}')
