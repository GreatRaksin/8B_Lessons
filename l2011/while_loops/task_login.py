login = input('Введите логин: ')
password = input('Введите пароль: ')

correct_l = 'Zodiac'
correct_p = 'Zodi6712'

while login != correct_l and password != correct_p:
    print('неверно!')

    login = input('Введите логин: ')
    password = input('Введите пароль: ')

else:
    print(f'Добро пожаловать, {login}!')