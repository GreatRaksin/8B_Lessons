n = int(input('Для какого числа нужна таблица? '))

for num in range(1, 10):
    print(f'{n} * {num} = {n * num};')
    print(n * num)