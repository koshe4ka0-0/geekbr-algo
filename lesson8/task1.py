#1. Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N,
# состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.

s = (input("Введите строку: "))

def number_of_subs(s):
    lst = []
    
    for j in range(len(s)):
        for i in range(j + 1, len(s) + 1):
            if len(s[j:i]) != len(s) and hash(s[j:i])  not in lst:
                lst.append(hash(s[j:i]))
    return len(lst)


print(number_of_subs(s))