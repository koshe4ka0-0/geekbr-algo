# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала 
# (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль 
# (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и
#  отдельно вывести наименования предприятий, чья прибыль ниже среднего.

from collections import namedtuple

number_of_companies = int(input("Введите количество предприятий: "))
New_company = namedtuple('New_company', 'name first_quarter second_quarter third_quarter fourth_quarter year')
list_of_companies = []
sum_ = 0

for i in range(0, number_of_companies):
    name = (input("Введите название компании: "))
    first_quarter = int(input(f'Введите прибыль предприятия "{name}" за первый квартал: '))
    second_quarter = int(input(f'Введите прибыль предприятия "{name}" за второй квартал: '))
    third_quarter = int(input(f'Введите прибыль предприятия "{name}" за третий квартал: '))
    fourth_quarter = int(input(f'Введите прибыль предприятия "{name}" за четвертый квартал: '))
    year = first_quarter + second_quarter + third_quarter + fourth_quarter

    company = New_company(name, first_quarter, second_quarter, third_quarter, fourth_quarter, year)

    sum_ += year

    list_of_companies.append(company)

sum_ /= number_of_companies
print(f'Средний годовой доход предприятий: {sum_}')

print("Предприятия, чья прибыль выше среднего: ")

for i in range(number_of_companies):
    if list_of_companies[i].year > sum_:
        print(f'Предприятие "{list_of_companies[i].name}". Прибыль: {list_of_companies[i].year}')

print("Предприятия, чья прибыль ниже среднего: ")

for i in range(number_of_companies):
    if list_of_companies[i].year < sum_:
        print(f'Предприятие "{list_of_companies[i].name}". Прибыль: {list_of_companies[i].year}')

 



