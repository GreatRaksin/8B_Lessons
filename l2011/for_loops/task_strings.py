for letter in 'Hello, World!':
    if letter in [' ', '.', ',', '!']:
        continue  # пропуск итерации
    elif letter == 'W':
        break  # искусственная остановка цикла
    else:
        print(letter)

