"""Task 4. Найти пиковые числа. Число называется пиковым, если количество десятков в нем
больше количества единиц и сотен"""

n = int(input('Введите трехзначное число: '))
d1 = n % 10  # нашел единицы -> 453 % 10 = 3
d2 = n % 100 // 10  # нашел десятки -> 453 % 100 = 53, 53 // 10 = 5
d3 = n // 100 # нашел сотни -> 500 // 100 = 5

if d3 < d2 > d1:
    print('Число пиковое!')
else:
    print('Число не пиковое!')
