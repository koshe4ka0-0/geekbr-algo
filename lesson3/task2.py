#Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в этих
#  позициях первого массива стоят четные числа.
from random import randint


SIZE = 10
max_item = 1000
array = [ randint(0, max_item) for _ in range(SIZE)]
print(array)

#indexes = []
#for i in range(SIZE):
#    if array[i] % 2 == 0:
#        indexes.append(i)
#print(indexes)

indexes = [i for i in range(SIZE) if array[i] % 2 == 0]
print(indexes)
