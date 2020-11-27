from random import randint

numbers = []
n = int(input('Сколько чисел нужно? '))
for x in range(n):
    numbers.append(randint(1, 99))

print(numbers)

odd_numbers = 0
even_numbers = 0

for i in numbers:
    if i % 2 == 0:
        even_numbers += 1
    else:
        odd_numbers += 1

print(f'Четных чисел {even_numbers},\nНечетных {odd_numbers}.')

