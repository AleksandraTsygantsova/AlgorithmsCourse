# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль
# за четыре квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple

Revenue = namedtuple('Revenue', 'company_name, revenue')
companies = []

companies_num = int(input('Введите кол-во предприятий: '))
revenue_sum = 0

for i in range(companies_num):
    company_name = input(f'Введите наименование {i+1} компании: ')
    revenue_data = []

    for k in range(4):
        revenue = float(input(f'Введите прибыль компании за {k+1} квартал: '))
        revenue_data.append(revenue)
        revenue_sum += revenue

    companies.append(Revenue(company_name, revenue_data)._asdict())

print('_' * 50)

average_revenue = revenue_sum / companies_num
print(f'Средняя прибыль за год для всех предприятий: {average_revenue}')

for company in companies:
    company_revenue = sum(company["revenue"])
    if company_revenue > average_revenue:
        print(f'Годовая прибыль компании {company["company_name"]} = {company_revenue} и на '
              f'{company_revenue - average_revenue} больше средней годовой прибыли всех предприятий')
    else:
        print(f'Годовая прибыль компании {company["company_name"]} = {company_revenue} и на '
              f'{average_revenue - company_revenue} меньше средней годовой прибыли всех предприятий')


