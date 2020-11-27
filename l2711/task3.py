from random import randint  # randint - случайное число

secret_num = randint(1, 101)  # загадываем число от 1 до 9
guess_num = 0  # сюда будем записывать числа, которые угадывают
attempts = 0  # храним количество попыток

while guess_num != secret_num and attempts < 6: # пока число не угадано и меньше 5 попыток
    attempts += 1  # добавляем одну попытку
    guess_num = int(input('Введите число от 1 до 10, пока не угадаете: '))
    """даем подсказки"""
    if guess_num > secret_num:  # если введенное число больше загаданного
        print('Число меньше!')
    else:
        print('Число больше!')

if guess_num == secret_num:
    print(f'Угадал за {attempts} попыток! Молодец!')
else:
    print(f'Не угадал! Я загадал число {secret_num}')
