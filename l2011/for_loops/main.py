'''
range(10) - [0, 1, ... 9]
range(1, 100) - [1, 2...99]
range(0, 100, 2) - [0, 2, 4, 6, ... 98]

range(start, stop, step)
'''
import time
n = int(input('Введите число: '))

for i in range(n, -1, -1):
    print(i)
    time.sleep(0.5)
    # print(f'управляющая переменная = {i}')
    # print('Hello, World!')