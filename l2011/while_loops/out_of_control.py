prompt = '\nTell me smth and i will repeat if back to u: '
prompt += '\nEnter "quit" to end the program'

active = True # <- флаг работы цикла
while active: # while active == True
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)