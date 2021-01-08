# 1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в
# рамках домашнего задания первых трех уроков.


# Задача:
# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
import random
import timeit

# Первый вариант реализации функции
# __________________________________

def find_max_neg_fst(array):
    neg_array = []
    for i in array:
        if i < 0:
            neg_array.append(i)

    max_neg = neg_array[0]
    for i in neg_array:
        if i < max_neg:
            max_neg = i

    max_neg_idx = neg_array.index(max_neg)
    return max_neg, max_neg_idx

# Второй вариант реализации функции
# __________________________________

def find_max_neg_snd(array):
    max_neg = array[0]
    for i in array:
        if i < max_neg and i < 0:
            max_neg = i

    max_neg_idx = array.index(max_neg)
    return max_neg, max_neg_idx

# Третий вариант реализации функции
# __________________________________

def find_max_neg_trd(array):
    neg_array = []
    for i in array:
        if i < 0:
            neg_array.append(i)
    max_neg = max(neg_array)
    max_neg_idx = array.index(max_neg)
    return max_neg, max_neg_idx

# Срвнение различных реализаций функции

NUMBER_EXECUTIONS = 1
array = [random.randint(-100, 100) for i in range(20)]
time1 = timeit.timeit(f'find_max_neg_fst({array})',
                      setup='from __main__ import find_max_neg_fst',
                      number=NUMBER_EXECUTIONS)
time2 = timeit.timeit(f'find_max_neg_snd({array})',
                      setup='from __main__ import find_max_neg_snd',
                      number=NUMBER_EXECUTIONS)
time3 = timeit.timeit(f'find_max_neg_trd({array})',
                      setup='from __main__ import find_max_neg_trd',
                      number=NUMBER_EXECUTIONS)

print(f'Вторая реализация функции быстрее первой в {round(time2 / time1, 2)} раза')
print(f'Третья реализация функции быстрее второй в {round(time3 / time2, 2)} раза')

# Вторая реализация функции быстрее первой в 0.53 раза
# Третья реализация функции быстрее второй в 1.56 раза