earnings = float(input('Выручка фирмы '))
costs = float(input('Издержки фирмы '))
if costs > earnings:
     print("Ваша фирма работает в убыток")
elif earnings > costs:
     profitability = round((earnings - costs) / earnings, 2)
     emp = int(input('Введите количество сотрудников - '))
     earn_emp = round((earnings / emp), 2)
     print(f'Рентабельность составила - {profitability}')
     print(f'Прибыль на 1 сотрудника - {earn_emp}')
