"""
DZ 3
Склонение слова.
Реализовать склонение слова «процент» во фразе «N процентов».
Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100
1 процент
2 процента
...
100 процентов
"""
for i in range(1, 101):
    if i % 10 == 1 and i != 11:
        ending = ''
    elif (i % 10 == 2 or i % 10 == 3 or i % 10 == 4) and i != 12 and i != 13 and i != 14:
        ending = 'а'
    else:
        ending = 'ов'
    print(i, 'процент' + ending)
