prev = cur = 1
element = int(input('Номер элемента: '))

print(prev, cur, end=' ')
for number in range(element - 2):
    prev, cur = cur, prev + cur
    print(cur, end=' ')
