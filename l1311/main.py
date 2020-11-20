age = int(input('Введите возраст: '))

if age <= 4:
    print('Доступ запрещен!')
elif age >= 5 or age <= 15: # 5 <= age <= 15
    print('Обратитесь за помощью к родителям!')
else:
    print('Доступ разрешен!')

'''
Задача1. Написать программу, которая проверяет, действительно ли
количество печенек больше 500 или меньше 100. В зависимости от этих
условий программа должна написать либо "слишком много", либо "слишком мало"
Если количество печенек от 100 до 500, написать "достаточно"

Задача 2. 
Программа должна проверять, может ли человек участвовать в соревновании.
Критерии:
Класс - старше 7го, средний балл - больше 7.7.
'''
grade = float(input('Введите средний балл: '))
if age >= 7:
    if grade >= 7.7:
        print('Вы проходите!')
else:
    print('Не проходите!')

'''
В магазине распродажа. На товары за 10$ и меньше скидка 10%, а на товары
дорож 10$ - 20%. Напишите порграмму, которая будет запрашивать цену товара
и показывать размер скидки (10 или 20%) и итоговую цену.
'''
price = float(input('Введите цену товара: '))

if price <= 10:
    print(f'Скидка 10%, итоговая цена: ${price * 0.9}')
else:
    print(f'Скидка 20%, итоговая цена: ${price * 0.8}')

'''
Task 4. Заданы две клетки шахматной доски. Если они покрашены в один цвет, 
то выведите слово YES, а если в разные цвета — то NO. 
Программа получает на вход четыре числа от 1 до 8 каждое, 
задающие номер столбца и номер строки сначала для первой клетки, 
потом для второй клетки.
'''

x1 = int(input('Введите координату: '))
x2 = int(input('Введите координату: '))
y1 = int(input('Введите координату: '))
y2 = int(input('Введите координату: '))

number = x1 + x2 + y1 + y2
if number % 2 == 0:
    print('Клетки одинаковые!')
else:
    print('Клетки не одинаковые!')

'''
Сколько чисел совпадает?
'''
a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)

'''
Проверка пароля
'''
password = input('Введите пароль: ')
correct_pass = 'QA6b150k'

if password in correct_pass:
    print('Вход...')
else:
    print('Пароль неправильный!')