#В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве. Вариант1

def func(array):

    max_ = float('-inf')
    max_index = -1

    for i in range(len(array)):
        if array[i] < 0 and array[i] > max_:
            max_index = i
            max_ = array[i]
    
    if max_index == -1:
        return 'В массиве не было ни одного отрицательного числа'
    else:
        return f'Максимальный отрицательный элемент массива : {max_}. Его индекс : {max_index}'


# 100 loops, best of 5: 2.84 usec per loop: 10
# 100 loops, best of 5: 11.5 usec per loop: 100
# 100 loops, best of 5: 97.5 usec per loop: 1000
# 100 loops, best of 5: 976 usec per loop: 10000
# 100 loops, best of 5: 10.1 msec per loop: 100000
# 100 loops, best of 5: 102 msec per loop: 1000000

#В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве. Вариант2

def func_2(array):

    buf  = list(array)
    buf.sort()
    i = 0

    if buf[i] >= 0:
        return 'В массиве не было ни одного отрицательного числа'

    else:
        for i, item in enumerate(buf):
            if item < 0:
                pass
            else:
                break
            
    return f'Максимальный отрицательный элемент массива : {buf[i - 1]}. Его индекс : {array.index(buf[i - 1])}'

# 100 loops, best of 5: 3.99 usec per loop: 10
# 100 loops, best of 5: 18.6 usec per loop: 100
# 100 loops, best of 5: 217 usec per loop: 1000
# 100 loops, best of 5: 2.84 msec per loop: 10000
# 100 loops, best of 5: 34.2 msec per loop: 100000
# 100 loops, best of 5: 569 msec per loop: 1000000

#Вариант 3
def func_3(array):

    buf = [ i for i in array if i < 0]

    if buf == []:
        return 'В массиве не было ни одного отрицательного числа'
    else:
        max_ = max(buf)
        return f'Максимальный отрицательный элемент массива : {max_}. Его индекс : {array.index(max_)}'

# 100 loops, best of 5: 4.92 usec per loop: 10
# 100 loops, best of 5: 24.5 usec per loop: 100
# 100 loops, best of 5: 165 usec per loop: 1000
# 100 loops, best of 5: 1.58 msec per loop: 10000
# 100 loops, best of 5: 14.8 msec per loop: 100000
# 100 loops, best of 5: 189 msec per loop: 1000000


from random import randint

SIZE = 10
max_item = 100000
min_item = -100000
    
array = [randint(min_item, max_item) for _ in range(SIZE)]


# Вывод: первый алгоритм работает быстрее. Он проходится по списку всего один раз. В свою очередь, второй алгоритм 
#проходится по массиву несколько раз: первый, чтобы отсортировать массив, второй раз он ищет первый положительный элемент массива,
#и последний раз, чтобы найти индекс элемента по его значению. Третий же алгоритм работает с массивом тоже три раза. Сначала чтобы 
#создать список из отрицательных элементов, потов чтобы найти максимальный элемент, а затем чтобы по значению определить индекс элемента.
#Возможно второй алгоритм работает меленнее третьего, потому что там присутствует копирование списка с помощью list(), для того чтобы
#изначальный список не сортировался вместе со вторым.
    