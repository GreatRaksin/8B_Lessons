'''
*
* *
* * *
* * * *
* * *
* *
*
'''

n = int(input('Сколько звезд нужно? '))

for i in range(n):  # генерирую линии из звездочек
    for j in range(i):  # генерирую звездочки
        print('⭐️ ', end='')
    print('')
for i in range(n, 0, -1):
    for j in range(i):
        print('⭐️ ', end='')
    print('')