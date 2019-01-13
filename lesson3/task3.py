# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
from random import randint

SIZE = 10
min_item = - 1000
max_item = 1000
array = [randint(min_item, max_item) for _ in range(SIZE)]
print(array)

max_ = min_item
min_ = max_item
max_index = 0
min_index = 0

for i in range(SIZE):
    if array[i] > max_:
        max_ = array[i]
        max_index = i

    if array[i] < min_:
        min_ = array[i]
        min_index = i

print(f'Максимальный элемент массива : {max_}')
print(f'Минимальный элемент массива : {min_}')

array[max_index], array[min_index] = array[min_index], array[max_index]
print(array)