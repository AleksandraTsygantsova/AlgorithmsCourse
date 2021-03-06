# 2. По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b,
# проходящей через эти точки.

x1, y1 = input('Введите координаты точки "a" через пробел: ').split()
x2, y2 = input('Введите координаты точки "b" через пробел: ').split()
x1, y1, x2, y2 = float(x1), float(y1), float(x2), float(y2)

k = (y1 - y2) / (x1 - x2)
b = y2 - k * x2

print(f'Уравнение прямой для точки a{x1, y1} и точки b{x2, y2}: y = {k}x + ({b})')
