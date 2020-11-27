from random import randint  # randint - случайное число

secret_num = randint(1, 10)  # загадываем число от 1 до 9
guess_num = 0  # сюда будем записывать числа, которые угадывают
attempts = 0

while guess_num != secret_num and attempts < 5:
    attempts += 1
    guess_num = int(input('Введите число от 1 до 10, пока не угадаете: '))


if guess_num == secret_num:
    print('Угадал! Молодец!')
else:
    print(f'Я загадал число {secret_num}')
