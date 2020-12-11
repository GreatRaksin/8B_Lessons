a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

discr = b ** 2 - 4 * a * c
print(f'Дискриминант: {discr}')

if discr > 0:
    x1 = (-b + discr ** 0.5) / 2 * a
    x2 = (-b - discr ** 0.5) / 2 * a
    print(f'x1 = {round(x1, 2)}, x2 = {round(x2, 2)}')
elif discr == 0:
    x = -b / 2 * a
    print(f'x = {round(x, 2)}')
else:
    print('Корней нет')