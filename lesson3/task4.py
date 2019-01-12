#Определить, какое число в массиве встречается чаще всего.
from random import randint

SIZE = 10
max_item = 500000000
min_item = -50000000
array = [randint(min_item, max_item) for _ in range(SIZE)]
print(array)
max_ = 0

for i in range(min_item, max_item + 1):
    counter = 0
    for item in array:
        if item == i:
            counter += 1
    if counter > max_:
        digit = i
        max_ = counter

if max_ == 1:
    print('Все числа уникальны')
else:
    print(f'Число {digit} встречается в массиве чаще всего. Количество {digit} : {max_}')