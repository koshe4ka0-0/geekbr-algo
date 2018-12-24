# Найти сумму и произведение цифр введённого пользователем трехзначного числа

number = int(input('Введите трехзначное число: '))

num1 = number % 10
num2 = number // 10 % 10
num3 = number // 100

sum = num1 + num2 + num3
mult = num1 * num2 * num3

print(f'Сумма цифр числа {number} = {sum}')
print(f'Произведение цифр числа {number}= {mult}')
