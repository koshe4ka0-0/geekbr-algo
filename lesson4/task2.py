# [0, 1, 2, 3, 4, 5] len() == 6 last index == 5 .... [2, 3, 5, 7, 11, 13, 17] 3 -- > 5 [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
# 11 --> 31 
import cProfile

# Задание2 с решетом Эратосфена
def with_eratostenes(index):
    SIZE = 1000
    array = [ i for i in range(SIZE)]
    
    def sito_eratostensa(sieve):
        sieve[1] = 0
    
        for i in range(2, len(sieve)):
            if sieve[i] != 0:
                j = i + i
                while j < len(sieve):
                    sieve[j] = 0
                    j += i
    
        result = [i for i in sieve if i != 0]
        return result

    simple = sito_eratostensa(array)
    last = SIZE - 1

    while len(simple) < index:
        for _ in range(SIZE):
            last += 1
            array.append(last)

        simple = sito_eratostensa(array)

    return simple[index -1]

#cProfile.run('with_eratostenes(10000)')

#ncalls  tottime  percall  cumtime  percall filename:lineno(function) (10)
#       1    0.000    0.000    0.000    0.000 task2.py:19(<listcomp>)
#        1    0.000    0.000    0.001    0.001 task2.py:5(with_eratostenes)
#        1    0.000    0.000    0.000    0.000 task2.py:7(<listcomp>)
#        1    0.000    0.000    0.001    0.001 task2.py:9(sito_eratostensa)

#ncalls  tottime  percall  cumtime  percall filename:lineno(function) (100)
#        1    0.000    0.000    0.000    0.000 task2.py:19(<listcomp>)
#        1    0.000    0.000    0.001    0.001 task2.py:5(with_eratostenes)
#        1    0.000    0.000    0.000    0.000 task2.py:7(<listcomp>)
#        1    0.000    0.000    0.001    0.001 task2.py:9(sito_eratostensa)

#ncalls  tottime  percall  cumtime  percall filename:lineno(function) (1000)
#        8    0.001    0.000    0.001    0.000 task2.py:19(<listcomp>)
#        1    0.001    0.001    0.024    0.024 task2.py:5(with_eratostenes)
#        1    0.000    0.000    0.000    0.000 task2.py:7(<listcomp>)
#        8    0.017    0.002    0.022    0.003 task2.py:9(sito_eratostensa)

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)(10000)
#      105    0.127    0.001    0.127    0.001 task2.py:19(<listcomp>)
#        1    0.016    0.016    3.559    3.559 task2.py:5(with_eratostenes)
#        1    0.000    0.000    0.000    0.000 task2.py:7(<listcomp>)
#      105    2.669    0.025    3.537    0.034 task2.py:9(sito_eratostensa)


# 100 loops, best of 5: 447 usec per loop: 10
# 100 loops, best of 5: 455 usec per loop: 100
# 100 loops, best of 5: 17.5 msec per loop: 1000
# 100 loops, best of 5: 3.21 sec per loop: 10000

#Задание2 без решета Эратосфена

def without_eratostenes(index):
    sieve = [2, ]
    last = 2

    while len(sieve) != index:
        divide = 0
        last += 1

        for i in sieve: 
            if last % i == 0:
                divide += 1
                break

        if divide == 0:
            sieve.append(last)

    return sieve[-1]

# 100 loops, best of 5: 15.2 usec per loop: 10
# 100 loops, best of 5: 404 usec per loop: 100
# 100 loops, best of 5: 32.8 msec per loop: 1000
# 100 loops, best of 5: 11.2 sec per loop: 10000

#cProfile.run('without_eratostenes(10000)')       
#ncalls  tottime  percall  cumtime  percall filename:lineno(function) (10)
#        1    0.000    0.000    0.000    0.000 task2.py:86(without_eratostenes)

# ncalls  tottime  percall  cumtime  percall filename:lineno(function) (100)
#        1    0.000    0.000    0.000    0.000 task2.py:86(without_eratostenes)


#ncalls  tottime  percall  cumtime  percall filename:lineno(function) (1000)
#        1    0.034    0.034    0.035    0.035 task2.py:86(without_eratostenes)

#ncalls  tottime  percall  cumtime  percall filename:lineno(function) (10000)
#        1    2.335    2.335    2.343    2.343 task2.py:86(without_eratostenes)

def test_eratostensa(func):
    lst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]

    for i, item in enumerate(lst):
        assert item == func(i + 1)
        print(f'Test {i + 1} OK')

#test_eratostensa(with_eratostenes)
#test_eratostensa(without_eratostenes)

