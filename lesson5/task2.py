# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
# элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
# соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

a = input("Введите число в шестнадцатеричной системе счисления: ")
b = input("Введите число в шестнадцатеричной системе счисления: ")

#a = 'A2'
#b = 'C4F'

#a = '20A4'
#b = 'B15'

#a = '1C52'
#b = '891'

deq1 = deque(a)
deq2 = deque(b)

def in_hex(d):

    alf = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    for i in range(len(d)):
        for key, value in alf.items():
            if d[i] == value:
                d[i] = key
    return d

def sum_(a, b):


    if len(a) < len(b):
        while len(a) != len(b):
            a.appendleft('0')
    elif len(b) < len(a):
        while len(b) != len(a):
            b.appendleft('0')

    alf = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    a.reverse()
    b.reverse()
    carry = 0
    d = deque()

    for i in range(len(a)):
        result = alf[a[i]] + alf[b[i]] + carry

        if result > 15:
            carry = result // 16
        else:
            carry = 0
            
        d.appendleft(result % 16)
    if carry != 0:
        d.appendleft(carry)
        
    in_hex(d)
    
    a.reverse()
    b.reverse()

    return d

def mini_multiply(deq, number):

    alf = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    carry = 0
    d = deque()
    for i in deq:
        result = alf[i] * alf[number] + carry
        if result > 15:
            carry = result // 16
        else:
            carry = 0
        d.appendleft(result % 16)
    if carry != 0:
        d.appendleft(carry)

    return d

def multiply(deq2, deq1):
    
    deq2.reverse()
    deq1.reverse()
    result = deque()

    for c in range(len(deq2)):
        answer = mini_multiply(deq1, deq2[c])
        if c == 0:
            pass
        else:
            for i in range(c):
                answer.append(0)
    
        in_hex(answer)

        result = sum_(result, answer)
    deq2.reverse()
    deq1.reverse()
    return result
    
print(sum_(deq1, deq2))
print(multiply(deq1, deq2))
