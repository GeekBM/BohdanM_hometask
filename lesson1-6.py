distance = int(input('Дистанция в первый день - '))
goal = int(input('Цель - '))
day = 1
while distance < goal:
    day += 1
    distance *= 1.1
print(f'Необходимое количество дней {day}')