# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого)

print('Введите три разных числа: ')
num1 = int(input('Первое число: '))
num2 = int(input('Второе число: '))
num3 = int(input('Третье число: '))

if num1 < num2 < num3 or num3 < num2 < num1:
    print('Среднее число:', num2)
elif num2 < num1 < num3 or num3 < num1 < num2:
    print('Среднее число:', num1)
else:
    print('Среднее число:', num3)
