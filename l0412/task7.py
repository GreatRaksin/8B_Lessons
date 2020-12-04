"""Task 7. Посчитать факториал числа"""
# 5! = 1 * 2 * 3 * 4 * 5 = 120

n = int(input('Введите число: '))
f = 1

for number in range(1, n + 1):
    f *= number

print(f'{n}! = {f}')