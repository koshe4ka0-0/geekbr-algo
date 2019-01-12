#В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
from random import randint

SIZE = 10
max_item = 10
min_item = -10

array = [randint(min_item, max_item) for _ in range(SIZE)]
print(array)

max_ = min_item
max_index = -1

for i in range(SIZE):
    if array[i] < 0 and array[i] > max_:
        max_index = i
        max_ = array[i]

if max_index == -1:
    print('В массиве не было ни одного отрицательного числа')
else:
    print(f'Максимальный отрицательный элемент массива : {max_}. Его индекс : {max_index}')
