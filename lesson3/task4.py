#Определить, какое число в массиве встречается чаще всего.
from random import randint

SIZE = 10
max_item = 5
min_item = 1
array = [randint(min_item, max_item) for _ in range(SIZE)]
print(array)
max_ = 0

for i in range(max_item + 1):
    counter = 0
    for item in array:
        if item == i:
            counter += 1
    if counter > max_:
        digit = i
        max_ = counter

print(f'Число {digit} встречается в массиве чаще всего. Количество {digit} : {max_}')