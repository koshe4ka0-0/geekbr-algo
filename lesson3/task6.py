# Найти максимальный элемент среди минимальных элементов столбцов матрицы.
from random import randint

ROW = 5
COL = 3
min_item = -3
max_item = 7
matrix = [[randint(min_item, max_item) for i in range(COL)] for j in range(ROW)]

for i in matrix:
    print(i)

min_ = max_item
max_ = min_item

for i in range(COL):
    min_ = max_item
    for j in range(ROW):
        if matrix[j][i] < min_:
            min_ = matrix[j][i]
    if min_ > max_:
        max_ = min_

    print(f'Минимальный элемент {i + 1} столбца : {min_}')
print(f'Максимальный элемент среди минимальных элементов столбцов матрицы: {max_}')
    