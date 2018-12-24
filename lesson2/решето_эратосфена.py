number = int(input("Введите до какого числа вы хотите вывести простые числа:",))

sieve = [ i for i in range(number)]
print(sieve)

sieve[1] = 0

for i in range(2, number):
    if sieve[i] != 0:
        j = i + i
        while j < number:
            sieve[j] = 0
            j += i
print(sieve)

result = [i for i in sieve if i != 0]
print(result)