#Builtins
from datetime import *

# Own




time = str(datetime.now())
time = int(time[11:13])

if 5 <= time < 12:
    greeting = 'Bom dia!'
if 12 <= time < 18:
    greeting = 'Boa tarde!'
if 0 <= time < 5 or 18 <= time <= 24:
    greeting = 'Boa noite!'

print(f'\n\n\33[92m. . . cryptinpyc . . .\n{str(datetime.now())[0:22]}\n{greeting.center(22, " ")}\n......................\33[m\n\n\n"h" para ajuda;\n"e" para criptografar\n"d" para descriptografar\n\n')


def e():
    e_running = True
    while e_running:

        command_e = input('\33[92m\n:::Informe o caminho ou pressione "i" para criação instantânea:::\n[] >>> \33[m')
        if command_e.upper() == "I":
            msg = input('\33[92mDados: \33[m')
            e_running = False
        else:
            path = command_e
            e_running = False


def action():
    main_running = True
    while main_running:

        command = input('\33[92m[cryptinpyc] >>> \33[m')



        if command.upper() == 'H':
            print('\nHELP')
        if command.upper() == 'E':
            # from encrypt import *
            e()

        if command.upper() == 'D':
            pass

        if command.upper() == 'h':
            pass

        if command.upper().count('EXIT') > 0:
            main_running = False
            exit()



action()